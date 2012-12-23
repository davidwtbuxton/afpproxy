from __future__ import absolute_import
import unittest
from afpproxy import afp, dsi, proxy


class AFPNameTests(unittest.TestCase):
    def test_api(self):
        afp.take_name
        afp.AFPName
        obj = afp.AFPName()
        assert callable(obj)

    def test_short_name(self):
        name, data = afp.take_name('\x01\x08example')
        assert name == 'example'
        assert len(data) == 0
    
    def test_long_name(self):
        name, data = afp.take_name('\x02\x08example')
        assert name == 'example'
        assert len(data) == 0

    def test_utf8_name(self):
        name, data = afp.take_name('\x03\x00\x00\x01\x00\x00\x07example')
        assert name == 'example'
        assert len(data) == 0


class StructWithNamesTests(unittest.TestCase):
    def test_basic(self):
        s = afp.StructWithNames('!BIH')
        result = s.unpack('\x03\x00\x00\x04\xd2\x04\xd2')
        assert result == (3, 1234, 1234)


if __name__ == "__main__":
    unittest.main()
