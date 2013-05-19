from distutils.core import setup
import os

import afpproxy


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name = 'afpproxy',
    author = 'David Buxton',
    author_email = 'david@gasmark6.com',
    version = afpproxy.__version__,
    license = 'MIT',
    url = 'https://github.com/davidwtbuxton/afpproxy',
    description = 'proxy for the AFP (AppleShare) protocol',
    long_description = read('README.rst'),
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Twisted',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: Proxy Servers',
    ],
    scripts = ['bin/afpproxy'],
    packages = ['afpproxy'],
)
