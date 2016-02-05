from __future__ import absolute_import
import getopt
import logging
import sys

from twisted.internet import reactor

from afpproxy import __version__
from afpproxy.proxy import AFPProxyFactory
from afpproxy.afp import AFPLogger


DEFAULT_LOGLEVEL = logging.INFO


def configure_logging(loglevel=DEFAULT_LOGLEVEL):
    format = '%(asctime)s %(message)s'
    logging.basicConfig(level=loglevel, format=format)


def usage():
    sys.stderr.write(
        '%(prog)s version %(version)s\n'
        'Usage: %(prog)s [--debug] [--host <server>] [--port <port>] [--listen <port>]\n'
        % {'prog': 'afpproxy', 'version': __version__}
    )


def parse_command_line(argv):
    opts, args = getopt.getopt(argv, 'h:p:l:',
        ['help', 'debug', 'host=', 'port=', 'listen='])

    flags = {'loglevel': DEFAULT_LOGLEVEL}

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
        elif key in ('--debug',):
            flags['loglevel'] = logging.DEBUG

    return flags


def main():
    try:
        kwargs = parse_command_line(sys.argv[1:])
    except (ValueError, getopt.GetoptError):
        usage()
        return 1

    configure_logging(kwargs.pop('loglevel', DEFAULT_LOGLEVEL))

    run(**kwargs)

    return 0


def run(host='localhost', port=548, listen=5548):
    """Starts a proxy server.

    :param host: address or hostname of server to proxy.
    :param port: listening port of server to proxy.
    :param listen: port to listen for incoming connections.
    """
    # N.B. We create the proxy with an AFPLogger handler.
    logging.info('afpproxy version %s' % __version__)
    reactor.listenTCP(listen, AFPProxyFactory(host, port, handler=AFPLogger()))

    logging.info('Proxy connecting to %s port %s', host, port)
    logging.info('Proxy listening on port %s', listen)

    reactor.run()
