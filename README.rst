=========
AFPproxy
=========

AFPproxy is a proxy for an AppleShare file server. It is intended to help debug client/server connections on Mac OS X.

Installation
=============

Requires Python 2.5 or later and Twisted. AFPproxy does not run on Python 3. Mac OS X 10.5 and later include Python and Twisted by default.

You can download and install the source directly:

    tar -xf afpproxy-0.1.tar.gz
    cd afpproxy-0.1
    python setup.py install

Or install it from PyPI:

    pip install afpproxy

Usage
======

Once installed, or even if you are in the source directory, you can run afpproxy with:

    python -m afpproxy

By default this proxies your real AFP server on localhost port 548, and accepts connections on port 5548. You then connect to the running afpproxy and will see a description of the commands sent between client and server.

To proxy to a different server give its name or IP address:

    python -m afpproxy example.com

Or to proxy to a server running on a non-standard port:

    python -m afpproxy example.com 1234



