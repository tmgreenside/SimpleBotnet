from pexpect import pxssh

class Client:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s  #if login done.
        except Exception, e: # if fails
            print e
            print "[-] Error connecting"

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before # process results

def botnetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print "[*] output from " + client.host
        print "[+] " + output

def addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

botNet = [] # empty list of botNet clients
addClient("10.0.2.7","trevor","password")

botnetCommand('ls')
