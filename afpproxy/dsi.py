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
    """Represents a DSI command header struct."""
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
    """A DSILogger instance is a call-able that accepts 2 arguments: the address
    of the sender; and the sent data. It is called repeatedly as new data is
    received.

    Once the logger has buffered a complete DSI message (along with any payload)
    it calls its data handler with 3 arguments: the address of the sender; the
    bytes of the payload; and a DSIHeader instance giving the fields of the DSI
    struct.

    Because we are interested in actual AFP commands we only call the handler
    when there is a payload (an actual AFP command).
    """
    def __init__(self, prefix='', handler=None):
        self.dsi = DSIHeader(0, 0, 0, 0, 0, 0)
        self.state = 0
        self.buffer = StringIO()
        self.handler = handler or debug_dsi
        assert callable(self.handler)

    def __call__(self, addr, data):
        assert self.state >= 0

        # Call the handler with a complete buffered command.
        if not self.state:
            text = self.buffer.getvalue()
            logging.debug(repr(text))
            if text:
                # Reset the buffer for the next command then dispatch this one.
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
    """A command handler that logs the DSI command itself and ignores any AFP
    command. This can be used as the handler argument when creating a DSILogger
    instance.

    See the AFPLogger class for how to handle AFP commands properly.
    """
    info = dict(dsi)
    info.update({
        'command_name': DSI_COMMAND_NAMES.get(info['command']),
        'address': addr[0],
        'port': addr[1],
    })

    logging.debug(info)
