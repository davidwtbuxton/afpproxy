__version__ = '0.1'
from afpproxy.proxy import AFPProxyFactory
from twisted.internet import reactor
import logging


def configure_logging():
    logging.basicConfig(level=logging.DEBUG)


def main():
    import sys

    configure_logging()
    
    rhost = 'localhost'
    rport = 548
    
    lport = 5548
    
    if len(sys.argv) > 1:
        rhost = sys.argv[1]
        
    if len(sys.argv) == 3:
        rport = int(sys.argv[2])
    
    logging.info('Proxy connected to %s port %s', rhost, rport)
    logging.info('Proxy listening on port %s', lport)
    reactor.listenTCP(lport, AFPProxyFactory(rhost, rport))
    reactor.run()


if __name__ == "__main__":
    main()
