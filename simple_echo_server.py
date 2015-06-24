from twisted.internet import protocol, reactor

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        print(data.decode())
        if data.decode() == 'exit\n':
            self.transport.write(('Connection is close. Buy.\n').encode())
            self.transport.loseConnection()
        else: self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

reactor.listenTCP(9000, EchoFactory())
reactor.run()
