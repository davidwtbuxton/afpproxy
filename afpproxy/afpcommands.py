from __future__ import absolute_import
from . import constants
import struct
"""You can list all the available commands using this module's afp_commands
attribute which is built from the list of classes.
"""


class _AFPCommand(object):
    "Base class for afp commands."
    code = 0

    def request(self, data):
        """The request function MUST return a tuple with the first member an
        integer command code.
        """
        raise NotImplementedError
    
    def response(self, data):
        raise NotImplementedError


class FPByteRangeLock(_AFPCommand):
    code = 1
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPCloseVol(_AFPCommand):
    code = 2
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPCloseDir(_AFPCommand):
    code = 3
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPCloseFork(_AFPCommand):
    code = 4
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPCopyFile(_AFPCommand):
    code = 5
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPCreateDir(_AFPCommand):
    code = 6
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPCreateFile(_AFPCommand):
    code = 7
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPDelete(_AFPCommand):
    code = 8
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPEnumerate(_AFPCommand):
    code = 9
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPFlush(_AFPCommand):
    code = 10
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPFlushFork(_AFPCommand):
    code = 11
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPGetForkParms(_AFPCommand):
    code = 14
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPGetSrvrInfo(_AFPCommand):
    code = 15
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPGetSrvrParms(_AFPCommand):
    code = 16
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPGetVolParms(_AFPCommand):
    code = 17
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPLogin(_AFPCommand):
    code = 18
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPLoginCont(_AFPCommand):
    code = 19
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPLogout(_AFPCommand):
    code = 20
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPMapID(_AFPCommand):
    code = 21
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPMapName(_AFPCommand):
    code = 22
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPMoveAndRename(_AFPCommand):
    code = 23
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPOpenVol(_AFPCommand):
    code = 24
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPOpenDir(_AFPCommand):
    code = 25
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPOpenFork(_AFPCommand):
    code = 26
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPRead(_AFPCommand):
    code = 27
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPRename(_AFPCommand):
    code = 28
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPSetDirParms(_AFPCommand):
    code = 29
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPSetFileParms(_AFPCommand):
    code = 30
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPSetForkParms(_AFPCommand):
    code = 31
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPSetVolParms(_AFPCommand):
    code = 32
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPWrite(_AFPCommand):
    code = 33
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPGetFileDirParms(_AFPCommand):
    code = 34
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPSetFileDirParms(_AFPCommand):
    code = 35
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPChangePassword(_AFPCommand):
    code = 36
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPGetUserInfo(_AFPCommand):
    code = 37
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPGetSrvrMsg(_AFPCommand):
    code = 38
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPCreateId(_AFPCommand):
    code = 39
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPDeleteID(_AFPCommand):
    code = 40
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPResolveID(_AFPCommand):
    code = 41
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPExchangeFiles(_AFPCommand):
    code = 42
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPCatSearch(_AFPCommand):
    code = 43
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPOpenDT(_AFPCommand):
    code = 48
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPCloseDT(_AFPCommand):
    code = 49
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPGetIcon(_AFPCommand):
    code = 51
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPAddAPPL(_AFPCommand):
    code = 53
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPRemoveAPPL(_AFPCommand):
    code = 54
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPGetAPPL(_AFPCommand):
    code = 55
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPAddComment(_AFPCommand):
    code = 56
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPRemoveComment(_AFPCommand):
    code = 57
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPGetComment(_AFPCommand):
    code = 58
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPByteRangeLockExt(_AFPCommand):
    code = 59
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPReadExt(_AFPCommand):
    code = 60
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPWriteExt(_AFPCommand):
    code = 61
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPGetAuthMethods(_AFPCommand):
    code = 62
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPLoginExt(_AFPCommand):
    code = 63
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPGetSessionToken(_AFPCommand):
    code = 64
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPDisconnectOldSession(_AFPCommand):
    code = 65
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPEnumerateExt(_AFPCommand):
    code = 66
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPCatSearchExt(_AFPCommand):
    code = 67
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPEnumerateExt2(_AFPCommand):
    code = 68
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPGetExtAttr(_AFPCommand):
    code = 69
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPSetExtAttr(_AFPCommand):
    code = 70
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPRemoveExtAttr(_AFPCommand):
    code = 71
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPListExtAttrs(_AFPCommand):
    code = 72
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPGetACL(_AFPCommand):
    code = 73
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPSetACL(_AFPCommand):
    code = 74
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPAccess(_AFPCommand):
    code = 75
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPSpotlightRPC(_AFPCommand):
    code = 76
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPSyncDir(_AFPCommand):
    code = 78
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPSyncFork(_AFPCommand):
    code = 79
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPZzzzz(_AFPCommand):
    code = 122
    def request(self, data):
        pass

    def response(self, data):
        pass



class FPAddIcon(_AFPCommand):
    code = 192
    def request(self, data):
        pass

    def response(self, data):
        pass


class BadNameError(Exception):
    """Not a valid AFPName."""


class AFPName(object):
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
            if name_type == constants.kFPUTF8Name:
                name_type, encoding, length = self.UTF8Name.unpack(data[:self.UTF8Name.size])
                offset = self.UTF8Name.size + length
                parts = struct.unpack('!BIH%ss' % length, data[:offset])
            elif name_type in (constants.kFPShortName, constants.kFPLongName):
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


def make_command_map():
    "Returns a mapping of command codes to class names, class object tuples."
    # Run through all the things in this module and register those which are
    # sub-classes of _AFPCommand (but not _AFPCommand itself).
    import sys
    
    module = sys.modules[__name__]
    names = dir(module)
    
    mapping = {}
    
    for name in names:
        cls = getattr(module, name)
        try:
            if issubclass(cls, _AFPCommand):
                # The base _AFPCommand.code = 0, we don't want it.
                if cls.code != 0:
                    obj = cls()
                    mapping[obj.code] = (name, obj.request, obj.response)
        except TypeError:
            pass
    
    return mapping


#: A map of code numbers to a tuple of (name, request func, response func).
commands = make_command_map()


