import struct
import logging


# Map of AFP command code to function name, request format, response format.
afp_commands = {
    1: ('FPByteRangeLock', '!BBhii', '!i'), #  - deprecated in AFP3
    2: ('FPCloseVol', '!Bbh', None), # 
    3: ('FPCloseDir', '!BBhi', None), #  - deprecated
    4: ('FPCloseFork', '!BBh', None), # 
    5: ('FPCopyFile', '!BBhihi', None), # Then variable length name fields
    6: ('FPCreateDir', '!BBhi', '!'), # 
    7: ('FPCreateFile', '!B', '!'), # 
    8: ('FPDelete', '!B', '!'), # 
    9: ('FPEnumerate', '!B', '!'), #  - deprecated
    10: ('FPFlush', '!B', '!'), # 
    11: ('FPFlushFork', '!B', '!'), # 
    14: ('FPGetForkParms', '!B', '!'), # 
    15: ('FPGetSrvrInfo', '!B', '!ih'), # 
    16: ('FPGetSrvrParms', '!B', '!'), # 
    17: ('FPGetVolParms', '!B', '!'), # 
    18: ('FPLogin', '!B', '!'), # 
    19: ('FPLoginCont', '!B', '!'), # 
    20: ('FPLogout', '!B', '!'), # 
    21: ('FPMapID', '!B', '!'), # 
    22: ('FPMapName', '!B', '!'), # 
    23: ('FPMoveAndRename', '!B', '!'), # 
    24: ('FPOpenVol', '!B', '!'), # 
    25: ('FPOpenDir', '!B', '!'), #  - deprecated
    26: ('FPOpenFork', '!B', '!'), # 
    27: ('FPRead', '!B', '!'), # 
    28: ('FPRename', '!B', '!'), # 
    29: ('FPSetDirParms', '!B', '!'), # 
    30: ('FPSetFileParms', '!B', '!'), # 
    31: ('FPSetForkParms', '!B', '!'), # 
    32: ('FPSetVolParms', '!B', '!'), # 
    33: ('FPWrite', '!B', '!'), # 
    34: ('FPGetFileDirParms', '!B', '!'), # 
    35: ('FPSetFileDirParms', '!B', '!'), # 
    36: ('FPChangePassword', '!B', '!'), # 
    37: ('FPGetUserInfo', '!B', '!'), # 
    38: ('FPGetSrvrMsg', '!B', '!'), # 
    39: ('FPCreateId', '!B', '!'), #  - deprecated
    40: ('FPDeleteID', '!B', '!'), #  - deprecated
    41: ('FPResolveID', '!B', '!'), # 
    42: ('FPExchangeFiles', '!B', '!'), # 
    43: ('FPCatSearch', '!B', '!'), #  - deprecated in AFP3
    48: ('FPOpenDT', '!B', '!'), #  - deprecated in 10.6
    49: ('FPCloseDT', '!B', '!'), #  - deprecated in 10.6
    51: ('FPGetIcon', '!B', '!'), #  - deprecated in 10.6
    53: ('FPAddAPPL', '!B', '!'), #  - deprecated in 10.6
    54: ('FPRemoveAPPL', '!B', '!'), #  - deprecated in 10.6
    55: ('FPGetAPPL', '!B', '!'), #  - deprecated in 10.6
    56: ('FPAddComment', '!B', '!'), #  - deprecated in 10.6
    57: ('FPRemoveComment', '!B', '!'), #  - deprecated in 10.6
    58: ('FPGetComment', '!B', '!'), #  - deprecated in 10.6
    59: ('FPByteRangeLockExt', '!B', '!'), # 
    60: ('FPReadExt', '!B', '!'), # 
    61: ('FPWriteExt', '!B', '!'), # 
    62: ('FPGetAuthMethods', '!B', '!'), #  - deprecated
    63: ('FPLoginExt', '!B', '!'), # 
    64: ('FPGetSessionToken', '!B', '!'), # 
    65: ('FPDisconnectOldSession', '!B', '!'), # 
    66: ('FPEnumerateExt', '!B', '!'), #  - deprecated
    67: ('FPCatSearchExt', '!B', '!'), # 
    68: ('FPEnumerateExt2', '!B', '!'), # 
    69: ('FPGetExtAttr', '!B', '!'), # 
    70: ('FPSetExtAttr', '!B', '!'), # 
    71: ('FPRemoveExtAttr', '!B', '!'), # 
    72: ('FPListExtAttrs', '!B', '!'), # 
    73: ('FPGetACL', '!B', '!'), # 
    74: ('FPSetACL', '!B', '!'), # 
    75: ('FPAccess', '!B', '!'), #  check for permission
    76: ('FPSpotlightRPC', '!B', '!'),   # AFP 3.2+
    78: ('FPSyncDir', '!B', '!'), # AFP 3.2+
    79: ('FPSyncFork', '!B', '!'), # AFP 3.2+
    122: ('FPZzzzz', '!B', '!'), # 
    192: ('FPAddIcon', '!B', '!'), #  - deprecated in 10.6
}

AFP_FMT = '!B'
afp_header = struct.Struct(AFP_FMT)
filename_format = struct.Struct('!B')
UTF8 = 'UTF-8'


def compile_commands():
    for k, v in afp_commands.items():
        response = struct.Struct(v[2]) if v[2] else v[2]
        yield (k, (v[0], struct.Struct(v[1]), response))


class BadNameError(Exception):
    """Not a valid AFPName."""


class AFPName(object):
    kFPShortName = 1
    kFPLongName = 2
    kFPUTF8Name = 3
    # 1 byte type, 4 byte encoding, 2 byte length
    UTF8Name = struct.Struct('!BIH')
    # 1 byte type, 1 byte length
    PascalName = struct.Struct('!BB')
    
    def __call__(self, data):
        # All name types start with a byte indicating the type.
        try:
            name_type = struct.unpack('!B', data[:1])[0]
        except struct.error:
            raise BadNameError
        
        try:
            if name_type == self.kFPUTF8Name:
                name_type, encoding, length = self.UTF8Name.unpack(data[:self.UTF8Name.size])
                offset = self.UTF8Name.size + length
                parts = struct.unpack('!BIH%ss' % length, data[:offset])
            elif name_type in (self.kFPShortName, self.kFPLongName):
                name_type, length = self.PascalName.unpack(data[:self.PascalName.size])
                offset = self.PascalName.size + length
                parts = struct.unpack('!B%sp' % length, data[:offset])
            else:
                raise BadNameError
        except struct.error:
            raise BadNameError
        
        # AFP uses null-bytes in the path name as a directory separator.
        name = parts[-1].replace(chr(0), ':')
        # Ummm, the name is either unicode or some crazy Mac encoding that depends
        # on the volume or client encoding. So you choose.
        return name, data[offset:]


take_name = AFPName()

    
class AFPLogger(object):
    # Pre-cook a map of AFP command codes to Struct instances.
    _request_formats = dict(compile_commands())

    def __init__(self):
        self.command_history = {}
        self._method_cache = {}
        
    def __call__(self, addr, data, dsi):
        key = (dsi.request_id, dsi.command)
        
        if dsi.flags:
            # This is a response.
            request = self.command_history[key]
            # Now we have the request we can understand the response.
            response = self.parse_afp_response(request, data)
            logging.debug(response)
        else:
            # This is a request.
            self.command_history[key] = self.parse_afp_request(data)
            logging.debug("%r %r", key, self.command_history[key])
        
        
    def parse_afp_request(self, data):
        """Returns a tuple of (int, ...)."""
        command_code = afp_header.unpack(data[:1])[0]
        try:
            command_name, method = self._method_cache[command_code]
        except KeyError:
            command_name, _ = afp_commands.get(command_code, command_code)
            method = getattr(self, command_name, None)
            self._method_cache[command_code] = (command_name, method)
        
        return method(data)

    def parse_afp_response(response, data):
        pass

    def unpack_afp_request(self, data):
        code = afp_header.unpack(data[:1])
        format = self._request_formats[code]
        return format.unpack(data[:format.size])

    def FPGetSrvrParms(self, data):
        parts = self.unpack_afp_request(data)
    
