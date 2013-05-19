from __future__ import absolute_import
import unittest

from afpproxy import afp, afpcommands, dsi, proxy


class AFPNameTests(unittest.TestCase):
    def test_api(self):
        afpcommands.take_name
        afpcommands.AFPName
        obj = afpcommands.AFPName()
        assert callable(obj)

    def test_short_name(self):
        name, data = afpcommands.take_name('\x01\x08example')
        assert name == 'example'
        assert len(data) == 0

    def test_long_name(self):
        name, data = afpcommands.take_name('\x02\x08example')
        assert name == 'example'
        assert len(data) == 0

    def test_utf8_name(self):
        name, data = afpcommands.take_name('\x03\x00\x00\x01\x00\x00\x07example')
        assert name == 'example'
        assert len(data) == 0


if __name__ == "__main__":
    unittest.main()
