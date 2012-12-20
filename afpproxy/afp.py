import struct
import logging


afp_commands = {
    1: 'FPByteRangeLock', #  - deprecated in AFP3
    2: 'FPCloseVol', # 
    3: 'FPCloseDir', #  - deprecated
    4: 'FPCloseFork', # 
    5: 'FPCopyFile', # 
    6: 'FPCreateDir', # 
    7: 'FPCreateFile', # 
    8: 'FPDelete', # 
    9: 'FPEnumerate', #  - deprecated
    10: 'FPFlush', # 
    11: 'FPFlushFork', # 
    14: 'FPGetForkParms', # 
    15: 'FPGetSrvrInfo', # 
    16: 'FPGetSrvrParms', # 
    17: 'FPGetVolParms', # 
    18: 'FPLogin', # 
    19: 'FPLoginCont', # 
    20: 'FPLogout', # 
    21: 'FPMapID', # 
    22: 'FPMapName', # 
    23: 'FPMoveAndRename', # 
    24: 'FPOpenVol', # 
    25: 'FPOpenDir', #  - deprecated
    26: 'FPOpenFork', # 
    27: 'FPRead', # 
    28: 'FPRename', # 
    29: 'FPSetDirParms', # 
    30: 'FPSetFileParms', # 
    31: 'FPSetForkParms', # 
    32: 'FPSetVolParms', # 
    33: 'FPWrite', # 
    34: 'FPGetFileDirParms', # 
    35: 'FPSetFileDirParms', # 
    36: 'FPChangePassword', # 
    37: 'FPGetUserInfo', # 
    38: 'FPGetSrvrMsg', # 
    39: 'FPCreateId', #  - deprecated
    40: 'FPDeleteID', #  - deprecated
    41: 'FPResolveID', # 
    42: 'FPExchangeFiles', # 
    43: 'FPCatSearch', #  - deprecated in AFP3
    48: 'FPOpenDT', #  - deprecated in 10.6
    49: 'FPCloseDT', #  - deprecated in 10.6
    51: 'FPGetIcon', #  - deprecated in 10.6
    53: 'FPAddAPPL', #  - deprecated in 10.6
    54: 'FPRemoveAPPL', #  - deprecated in 10.6
    55: 'FPGetAPPL', #  - deprecated in 10.6
    56: 'FPAddComment', #  - deprecated in 10.6
    57: 'FPRemoveComment', #  - deprecated in 10.6
    58: 'FPGetComment', #  - deprecated in 10.6
    59: 'FPByteRangeLockExt', # 
    60: 'FPReadExt', # 
    61: 'FPWriteExt', # 
    62: 'FPGetAuthMethods', #  - deprecated
    63: 'FPLoginExt', # 
    64: 'FPGetSessionToken', # 
    65: 'FPDisconnectOldSession', # 
    66: 'FPEnumerateExt', #  - deprecated
    67: 'FPCatSearchExt', # 
    68: 'FPEnumerateExt2', # 
    69: 'FPGetExtAttr', # 
    70: 'FPSetExtAttr', # 
    71: 'FPRemoveExtAttr', # 
    72: 'FPListExtAttrs', # 
    73: 'FPGetACL', # 
    74: 'FPSetACL', # 
    75: 'FPAccess', #  check for permission
    76: 'FPSpotlightRPC',   # AFP 3.2+
    78: 'FPSyncDir', # AFP 3.2+
    79: 'FPSyncFork', # AFP 3.2+
    122: 'FPZzzzz', # 
    192: 'FPAddIcon', #  - deprecated in 10.6
}

AFP_FMT = '!B'
afp_header = struct.Struct(AFP_FMT)


class AFPLogger(object):
    def __init__(self):
        self.command_history = {}
        
    def __call__(self, addr, data, dsi):
        key = (dsi.request_id, dsi.command)
        
        if dsi.flags:
            # This is a response.
            afp_command = self.command_history[key]
        else:
            # This is a request.
            self.command_history[key] = self.parse_afp_command(data)
        
        
    def parse_afp_command(self, data):
        """Returns a tuple of (int, ...)."""
        afp_command = afp_header.unpack(data[:1])[0]
        command_name = afp_commands.get(afp_command, afp_command)
        logging.debug(command_name)
        
    
