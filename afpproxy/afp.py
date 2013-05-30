from __future__ import absolute_import
import struct
import logging

from . import afpcommands
from . import constants


class AFPLogger(object):
    """An AFPLogger instance is called repeatedly with 3 arguments: the address
    of the sender; the AFP command data (comprising any AFP command header and
    its payload); and the DSI header for the AFP command.
    """
    # First byte of the data is the AFP command code.
    _command_code = struct.Struct('!B')

    def __init__(self):
        # As requests arrive we record them so that we can match a subsequent
        # response with the request that prompted it.
        self._command_history = {}

    def __call__(self, addr, data, dsi):
        key = (dsi.request_id, dsi.command)

        # DSICommand means this is an AFP command. Other commands like tickle
        # we ignore.
        if dsi.command == constants.kDSICommand:
            if dsi.flags:
                # This is a response.
                command_code = self._command_history[key][0]

                if dsi.error:
                    # Error! I might be very wrong but though the docs say this
                    # is uint32 it is actually a signed int. Meanwhile the same
                    # field is used for the write offset on requests and that
                    # time it actually is uint32.
                    error = struct.unpack('!i', struct.pack('!I', dsi.error))[0]
                    errname = constants.errors.get(error, error)
                    logging.info("%r %r %r", key, error, errname)
                else:
                    # Now we have the request we can understand the response.
                    response = self.response(command_code, data)
                    logging.info("%r %r", key, response)
            else:
                # This is a request.
                command_code = self._command_code.unpack(data[:1])[0]
                request = self.request(command_code, data)
                # The request MUST return a tuple with a valid command code
                assert isinstance(request, tuple), command_code
                assert request[0] == command_code, command_code

                # Record the request so that when a response arrives we know how
                # to interpret it.
                self._command_history[key] = request
                name = afpcommands.commands[command_code][0]
                logging.info("%r %r %r", key, name, request)

    def request(self, command_code, data):
        """Decodes any AFP request. Returns a tuple.

        The first member of the tuple must be an AFP command code.
        """
        name, request_func, response_func = afpcommands.commands[command_code]
        return request_func(data)

    def response(self, command_code, data):
        """Decodes any AFP response. Returns a tuple."""
        name, request_func, response_func = afpcommands.commands[command_code]
        return response_func(data)


