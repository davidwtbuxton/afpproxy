import getopt
import logging
import sys

from twisted.internet import reactor

from afpproxy.proxy import AFPProxyFactory
from afpproxy.afp import AFPLogger


__version__ = '0.1.1'


def configure_logging():
    format = '%(asctime)s %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=format)


def usage():
    sys.stderr.write(
        '%(prog)s version %(version)s\n'
        'Usage: %(prog)s [--host <server>] [--port <port>] [--listen <port>]\n'
        % {'prog': 'afpproxy', 'version': __version__}
    )


def parse_command_line(argv):
    opts, args = getopt.getopt(argv, 'h:p:l:', ['help', 'host=', 'port=', 'listen='])

    flags = {}

    for key, value in opts:
        if key in ('--help',):
            usage()
            raise SystemExit(2)
        elif key in ('-h', '--host'):
            flags['host'] = value
        elif key in ('-p', '--port'):
            flags['port'] = int(value)
        elif key in ('-l', '--listen'):
            flags['listen'] = int(value)

    return flags


def main():
    configure_logging()
    try:
        kwargs = parse_command_line(sys.argv[1:])
    except ValueError:
        usage()
        return 1

    run(**kwargs)

    return 0


def run(host='localhost', port=548, listen=5548):
    """Starts a proxy server.

    :param host: address or hostname of server to proxy.
    :param port: listening port of server to proxy.
    :param listen: port to listen for incoming connections.
    """
    logging.info('afpproxy version %s' % __version__)
    reactor.listenTCP(listen, AFPProxyFactory(host, port, handler=AFPLogger()))

    logging.info('Proxy connecting to %s port %s', host, port)
    logging.info('Proxy listening on port %s', listen)

    reactor.run()
