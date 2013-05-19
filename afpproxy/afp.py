from __future__ import absolute_import
import struct
import logging

from . import afpcommands
from . import constants


UTF8 = 'UTF-8'


class AFPLogger(object):
    # Pre-cook a map of AFP command codes to Struct instances.
    _command_code = struct.Struct('!B')

    def __init__(self):
        self._command_history = {}

    def __call__(self, addr, data, dsi):
        key = (dsi.request_id, dsi.command)

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
                    logging.debug("%r %r %r", key, error, errname)
                else:
                    # Now we have the request we can understand the response.
                    response = self.response(command_code, data)
                    logging.debug("%r %r", key, response)
            else:
                # This is a request.
                command_code = self._command_code.unpack(data[:1])[0]
                request = self.request(command_code, data)
                # The request MUST return a tuple with a valid command code
                assert isinstance(request, tuple), command_code
                assert request[0] == command_code, command_code

                self._command_history[key] = request
                name = afpcommands.commands[command_code][0]
                logging.debug("%r %r %r", key, name, request)


    def request(self, command_code, data):
        """Returns a tuple of (int, ...).

        The first member of the tuple must be an AFP command code.
        """
        name, request_func, response_func = afpcommands.commands[command_code]
        return request_func(data)

    def response(self, command_code, data):
        name, request_func, response_func = afpcommands.commands[command_code]
        return response_func(data)


