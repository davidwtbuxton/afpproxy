from __future__ import absolute_import
from cStringIO import StringIO
import logging
import struct

from .constants import (kDSICloseSession, kDSICommand, kDSIGetStatus,
    kDSIOpenSession, kDSITickle, kDSIWrite, kDSIAttention)

# DSI format is 16 bytes
# 1 byte request/response flag
# 1 byte command code
# 2 bytes request ID
# 4 bytes error code or data offset
# 4 bytes size of data
# 4 bytes reserved
# then the payload, if any
DSI_HEADER_FMT = '!BBHIII'

# Slightly friendlier names for the command codes.
DSI_COMMAND_NAMES = {
    kDSICloseSession: 'CLO',
    kDSICommand: 'COM',
    kDSIGetStatus: 'STA',
    kDSIOpenSession: 'OPE',
    kDSITickle: 'TIC',
    kDSIWrite: 'WRI',
    kDSIAttention: 'ATT',
}


class DSIHeader(object):
    __slots__ = ['flags', 'command', 'request_id', 'offset', 'length', 'reserved']
    format = struct.Struct(DSI_HEADER_FMT)

    def __init__(self, flags, command, request_id, offset, length, reserved):
        self.flags = flags
        self.command = command
        self.request_id = request_id
        self.offset = offset
        self.length = length
        self.reserved = reserved

    def __iter__(self):
        # Allows one to use dict() to convert the tuple to a dict.
        for key in self.__slots__:
            yield (key, getattr(self, key))

    @property
    def error(self):
        # Alias for offset
        return self.offset

    @classmethod
    def unpack(cls, data):
        args = cls.format.unpack(data[:cls.format.size])
        return cls(*args)


class DSILogger(object):
    def __init__(self, prefix='', handler=None):
        self.dsi = DSIHeader(0, 0, 0, 0, 0, 0)
        self.state = 0
        self.buffer = StringIO()
        self.handler = handler or debug_dsi
        assert callable(self.handler)

    def __call__(self, addr, data):
        assert self.state >= 0

        # Handle a complete buffered command.
        if not self.state:
            text = self.buffer.getvalue()
            if text:
                self.buffer.seek(0)
                self.buffer.truncate()
                self.handler(addr, text, self.dsi)

        # Parse and buffer a new command.
        if not self.state:
            self.dsi = DSIHeader.unpack(data)
            self.state = self.dsi.length
            # Discard the DSI header.
            data = data[DSIHeader.format.size:]

        # Buffer the new data and update the state pointer.
        payload, extra = data[:self.state], data[self.state:]
        self.state = self.state - len(payload)
        self.buffer.write(payload)

        # More than one DSI message in this data.
        if extra:
            self(addr, extra)


def debug_dsi(addr, data, dsi):
    info = dict(dsi)
    info.update({
        'command_name': DSI_COMMAND_NAMES.get(info['command']),
        'address': addr[0],
        'port': addr[1],
    })

    logging.debug(info)
