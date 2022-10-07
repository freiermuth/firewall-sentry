import os
from FirewallSentry import FirewallSentry
from flask import Flask, render_template, request

app = Flask(__name__)
sentry = FirewallSentry(os.environ["TOKEN"])


@app.route("/", methods=["GET", "POST"])
def firewall_manager():
    """
    Function to handle /
    :return: rendered /
    """
    blank = ""
    if request.method == "GET":
        print(F"Sentry Token: {sentry.get_token()}; Provided headers{request.headers}")
        if "FS-TOKEN" in request.headers and request.headers["FS-TOKEN"] == sentry.get_token():
            print("FS-TOKEN provided by {} is correct, returning list".format(request.remote_addr))
            return sentry.list()

    elif request.method == "POST":
        if "FS-TOKEN" in request.headers and request.headers["FS-TOKEN"] == sentry.get_token():
            if 'FS-HOST' in request.headers:
                sentry.update(request.headers["FS-HOST"], request.headers["X-Forwarded-For"])
                print("FS-TOKEN provided by {} is correct, host {} updated to {}".format(
                    request.headers["X-Forwarded-For"],
                    request.headers["FS-HOST"],
                    request.headers["X-Forwarded-For"]
                ))

            else:
                print("FS-TOKEN provided by {} is correct, but no FS-HOST provided".format(request.remote_addr))

        else:
            print("Header provided by {} is incorrect".format(request.remote_addr))

    return blank

if __name__ == "__main__":
    print("Development server detected")
    print("Token: " + sentry.get_token())

    app.run(debug=True, host="0.0.0.0", port=8080, use_reloader=False)