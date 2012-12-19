from string import printable
from twisted.internet import protocol
from twisted.protocols import portforward
from twisted.python import log
import logging
import pdb
import struct
import string


kFPGetSrvrInfo = 15


# DSI format is 16 bytes
# 1 byte request/response flag
# 1 byte command code
# 2 bytes request ID
# 4 bytes error code or data offset
# 4 bytes size of data
# 4 bytes reserved
# then the payload, if any
DSI_HEADER_FMT = '!BBHIII'
dsi_header = struct.Struct(DSI_HEADER_FMT)

DSI_CMDS = {
    0: '  0',
    1: 'CLO',
    2: 'COM',
    3: 'STA',
    4: 'OPE',
    5: 'TIC',
    6: 'WRI',
    8: 'ATT',
}

afp_commands = {
    1: 'kFPByteRangeLock', #  - deprecated in AFP3
    2: 'kFPCloseVol', # 
    3: 'kFPCloseDir', #  - deprecated
    4: 'kFPCloseFork', # 
    5: 'kFPCopyFile', # 
    6: 'kFPCreateDir', # 
    7: 'kFPCreateFile', # 
    8: 'kFPDelete', # 
    9: 'kFPEnumerate', #  - deprecated
    10: 'kFPFlush', # 
    11: 'kFPFlushFork', # 
    14: 'kFPGetForkParms', # 
    15: 'kFPGetSrvrInfo', # 
    16: 'kFPGetSrvrParms', # 
    17: 'kFPGetVolParms', # 
    18: 'kFPLogin', # 
    19: 'kFPLoginCont', # 
    20: 'kFPLogout', # 
    21: 'kFPMapID', # 
    22: 'kFPMapName', # 
    23: 'kFPMoveAndRename', # 
    24: 'kFPOpenVol', # 
    25: 'kFPOpenDir', #  - deprecated
    26: 'kFPOpenFork', # 
    27: 'kFPRead', # 
    28: 'kFPRename', # 
    29: 'kFPSetDirParms', # 
    30: 'kFPSetFileParms', # 
    31: 'kFPSetForkParms', # 
    32: 'kFPSetVolParms', # 
    33: 'kFPWrite', # 
    34: 'FPGetFileDirParms', # 
    35: 'kFPSetFileDirParms', # 
    36: 'kFPChangePassword', # 
    37: 'kFPGetUserInfo', # 
    38: 'kFPGetSrvrMsg', # 
    39: 'kFPCreateId', #  - deprecated
    40: 'kFPDeleteID', #  - deprecated
    41: 'kFPResolveID', # 
    42: 'kFPExchangeFiles', # 
    43: 'kFPCatSearch', #  - deprecated in AFP3
    48: 'kFPOpenDT', #  - deprecated in 10.6
    49: 'kFPCloseDT', #  - deprecated in 10.6
    51: 'kFPGetIcon', #  - deprecated in 10.6
    53: 'kFPAddAPPL', #  - deprecated in 10.6
    54: 'kFPRemoveAPPL', #  - deprecated in 10.6
    55: 'kFPGetAPPL', #  - deprecated in 10.6
    56: 'kFPAddComment', #  - deprecated in 10.6
    57: 'kFPRemoveComment', #  - deprecated in 10.6
    58: 'kFPGetComment', #  - deprecated in 10.6
    59: 'kFPByteRangeLockExt', # 
    60: 'kFPReadExt', # 
    61: 'kFPWriteExt', # 
    62: 'kFPGetAuthMethods', #  - deprecated
    63: 'kFPLoginExt', # 
    64: 'kFPGetSessionToken', # 
    65: 'kFPDisconnectOldSession', # 
    66: 'kFPEnumerateExt', #  - deprecated
    67: 'kFPCatSearchExt', # 
    68: 'kFPEnumerateExt2', # 
    69: 'kFPGetExtAttr', # 
    70: 'kFPSetExtAttr', # 
    71: 'kFPRemoveExtAttr', # 
    72: 'kFPListExtAttrs', # 
    73: 'kFPGetACL', # 
    74: 'kFPSetACL', # 
    75: 'kFPAccess', #  check for permission
    76: 'FPSpotlightRPC',   # AFP 3.2+
    78: 'FPSyncDir', # AFP 3.2+
    79: 'FPSyncFork', # AFP 3.2+
    122: 'kFPZzzzz', # 
    192: 'kFPAddIcon', #  - deprecated in 10.6
}

AFP_FMT = '!B'
afp_header = struct.Struct(AFP_FMT)


printable_map = dict((ord(c), c) for c in string.printable)


class DSILogger(object):
    
    def __init__(self, prefix=''):
        self.prefix = prefix
        self.state = 0
        self.request_id = 0
        self.command = 0
        self.flags = 0
        
    def __call__(self, data):
        pretty_data = str(len(data)).ljust(10)
        
        if self.state:
            logging.debug('%sData %s, need %s', self.prefix, pretty_data, self.state)
            payload, extra = data[:self.state], data[self.state:]
            self.state = self.state - len(payload)
            assert self.state >= 0
            

        else:
            hdr = dsi_header.unpack(data[:dsi_header.size])
            self.flags = hdr[0]
            self.command = hdr[1]
            self.request_id = hdr[2]
            size = hdr[4]
            payload = data[dsi_header.size:dsi_header.size + size]
            self.state = size - min(size, len(payload)) # Only count data we have.
            assert self.state >= 0
            logging.debug('%sData %s, command %s, size %s, state %s', self.prefix, pretty_data, self.command, size, self.state)
            
            if size and payload:
                command_code = afp_header.unpack(payload[:1])[0]
                logging.info('%sAFP command %s', self.prefix, afp_commands.get(command_code, command_code))
            extra = data[dsi_header.size + size:]

        if extra:
            logging.debug('Extra data!')
            self(extra)


class AFPProxyClient(portforward.ProxyClient):
    def __init__(self, *args, **kwargs):
        self.log = DSILogger(prefix='< ')

    def dataReceived(self, data):
        self.log(data)
        return portforward.ProxyClient.dataReceived(self, data)


class AFPProxyClientFactory(portforward.ProxyClientFactory):
    protocol = AFPProxyClient


class AFPProxy(portforward.ProxyServer):
    clientProtocolFactory = AFPProxyClientFactory
    
    def __init__(self, *args, **kwargs):
        self.log = DSILogger(prefix='> ')
        
    def dataReceived(self, data):
        self.log(data)
        return portforward.ProxyServer.dataReceived(self, data)


class AFPProxyFactory(portforward.ProxyFactory):
    protocol = AFPProxy

