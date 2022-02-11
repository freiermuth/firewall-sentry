from flask import Flask, render_template, request
import os
from FirewallSentry import FirewallSentry

app = Flask(__name__)
sentry = FirewallSentry(os.environ['TOKEN'])


@app.route("/", methods=['GET', 'POST'])
def ip():
    """
    Function to handle /
    :return: rendered /
    """
    blank = ''

    if request.method == 'GET':
        if 'FS_TOKEN' in request.headers and request.headers['FS_TOKEN'] == sentry.get_token():
            return sentry.list()

    elif request.method == 'POST':
        if 'FS_TOKEN' in request.headers and request.headers['FS_TOKEN'] == sentry.get_token():
            if 'FS_HOST' in request.headers:
                sentry.update(request.headers['FS_HOST'], request.remote_addr)
                print('FS_TOKEN provided by {} is correct, host {} updated to {}'.format(
                    request.remote_addr,
                    request.headers['FS_HOST'],
                    request.remote_addr
                ))

            else:
                print('FS_TOKEN provided by {} is correct, but no FS_HOST provided'.format(request.remote_addr))

        else:
            print('Header provided by {} is incorrect'.format(request.remote_addr))

    return blank

if __name__ == '__main__':
    print('Development server detected')
    print('Token: ' + sentry.get_token())

    app.run(debug=True, host='0.0.0.0', port=8080)