import os
import ipaddress
from FirewallSentry import FirewallSentry
from flask import Flask, render_template, request

app = Flask(__name__)
sentry = FirewallSentry(os.environ["TOKEN"])


def choose_ip(ip_list):
    for ip in ip_list:
        ip_parsed = ipaddress.ip_address(ip)
        if ip_parsed.is_private is not True:
            return ip

    return ip_list[0]


@app.route("/", methods=["GET", "POST"])
def firewall_manager():
    """
    Function to handle /
    :return: rendered /
    """
    blank = ""
    source_list = [x.strip() for x in request.headers["X-Forwarded-For"].split(',')]
    single_source = choose_ip(source_list)

    if request.method == "GET":
        if "FS-TOKEN" in request.headers and request.headers["FS-TOKEN"] == sentry.get_token():
            print("FS-TOKEN provided by {} is correct, returning list".format(single_source))
            return sentry.list()

    elif request.method == "POST":
        if "FS-TOKEN" in request.headers and request.headers["FS-TOKEN"] == sentry.get_token():
            if 'FS-HOST' in request.headers:
                sentry.update(request.headers["FS-HOST"], single_source)
                print("FS-TOKEN provided by {} is correct, host {} updated to {}".format(
                    single_source,
                    request.headers["FS-HOST"],
                    single_source
                ))

            else:
                print("FS-TOKEN provided by {} is correct, but no FS-HOST provided".format(single_source))

        else:
            print("Header provided by {} is incorrect".format(single_source))

    return blank

if __name__ == "__main__":
    print("Development server detected")
    print("Token: " + sentry.get_token())

    app.run(debug=True, host="0.0.0.0", port=8080, use_reloader=False)