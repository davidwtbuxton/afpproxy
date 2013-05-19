import logging

from twisted.internet import protocol
from twisted.protocols import portforward

from .dsi import DSILogger


class AFPProxyClient(portforward.ProxyClient):
    def __init__(self, *args, **kwargs):
        pass

    def dataReceived(self, data):
        addr = self.transport.addr
        self.factory.server.factory.dsi_logger(addr, data)
        return portforward.ProxyClient.dataReceived(self, data)


class AFPProxyClientFactory(portforward.ProxyClientFactory):
    protocol = AFPProxyClient


class AFPProxyServer(portforward.ProxyServer):
    clientProtocolFactory = AFPProxyClientFactory

    def dataReceived(self, data):
        addr = self.transport.client
        self.factory.dsi_logger(addr, data)
        return portforward.ProxyServer.dataReceived(self, data)


class AFPProxyFactory(portforward.ProxyFactory):
    protocol = AFPProxyServer

    def __init__(self, rhost, rport, handler=None):
        portforward.ProxyFactory.__init__(self, rhost, rport)
        self.dsi_logger = DSILogger(handler=handler)
