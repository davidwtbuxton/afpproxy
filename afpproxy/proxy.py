from .dsi import DSILogger
from twisted.internet import protocol
from twisted.protocols import portforward
from twisted.python import log


class AFPProxyClient(portforward.ProxyClient):
    def __init__(self, *args, **kwargs):
        self.log = DSILogger(prefix='< ')

    def dataReceived(self, data):
        self.log(data)
        return portforward.ProxyClient.dataReceived(self, data)


class AFPProxyClientFactory(portforward.ProxyClientFactory):
    protocol = AFPProxyClient


class AFPProxyServer(portforward.ProxyServer):
    clientProtocolFactory = AFPProxyClientFactory
    
    def __init__(self, *args, **kwargs):
        self.log = DSILogger(prefix='> ')
        
    def dataReceived(self, data):
        self.log(data)
        return portforward.ProxyServer.dataReceived(self, data)


class AFPProxyFactory(portforward.ProxyFactory):
    protocol = AFPProxyServer

