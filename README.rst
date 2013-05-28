=========
AFPproxy
=========

AFPproxy is an MIT licensed proxy for an AppleShare file server. You can use it to help debug client/server connections on Mac OS X, but I wrote it to explore the Twisted networking framework.

When running, the proxy prints details of the client/server communication to stderr.


Installation
=============

Requires Python 2.5 or later and Twisted. AFPproxy does not run on Python 3. Mac OS X 10.5 and later include Python and Twisted by default.

You can download and install the source directly::

    tar -xf afpproxy-0.1.tar.gz
    cd afpproxy-0.1
    python setup.py install

Or install it from PyPI::

    pip install afpproxy

If you don't have Twisted installed, install it. For Python 2.5 install it with::

    pip install 'Twisted<12.2' 'zope.interface<4'


Usage
======

Once installed, start the proxy with the ``afpproxy`` command.

By default this proxies your real AFP server on localhost port 548, and accepts connections on port 5548. You then connect to the running afpproxy and will see a description of the commands sent between client and server.

To proxy to a different server give its name or IP address::

    afpproxy --host example.com

Or to proxy to a server running on a non-standard port::

    afpproxy --host example.com --port 1234

To start a proxy listening for connections on port 1548::

    afpproxy --listen 1548


Development
===========

The source for afpproxy is hosted on GitHub: https://github.com/davidwtbuxton/afpproxy
