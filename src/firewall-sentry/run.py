import os
from FirewallSentry import FirewallSentry
from flask import Flask, render_template, request

app = Flask(__name__)
sentry = FirewallSentry(os.environ['TOKEN'])


@app.route('/', methods=['GET', 'POST'])
def firewall_manager():
    """
    Function to handle /
    :return: rendered /
    """
    blank = ''
    print(request.headers)
    if request.method == 'GET':
        print(F"Sentry Token: {sentry.get_token()}; Provided headers{request.headers}")
        if 'FS_TOKEN' in request.headers and request.headers['FS_TOKEN'] == sentry.get_token():
            print('FS_TOKEN provided by {} is correct, returning list'.format(request.remote_addr))
            return sentry.list()

    elif request.method == 'POST':
        print(request.headers)
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

    app.run(debug=True, host='0.0.0.0', port=8080, use_reloader=False)