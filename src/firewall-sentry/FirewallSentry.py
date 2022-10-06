

class FirewallSentry:

    def __init__(self, token):
        self.token = token
        self.hosts = {}

    def update(self, host, ip):
        self.hosts[host] = ip

    def list(self):
        if len(self.hosts) == 0:
            return ''

        else:
            s = "\r\n"
            return s.join(self.hosts.values())

    def get_token(self):
        return self.token
