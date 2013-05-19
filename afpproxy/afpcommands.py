from __future__ import absolute_import
from datetime import datetime, timedelta
import struct
import logging

from . import constants


"""You can list all the available commands using this module's afp_commands
attribute which is built from the list of classes.
"""

# Basic Python 2.5 version of built-in next(). Doesn't support sending in values.
try:
    next
except NameError:
    next = lambda x: x.next()


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
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPCloseVol(_AFPCommand):
    code = 2
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPCloseDir(_AFPCommand):
    code = 3
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPCloseFork(_AFPCommand):
    code = 4
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPCopyFile(_AFPCommand):
    code = 5
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPCreateDir(_AFPCommand):
    code = 6
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPCreateFile(_AFPCommand):
    code = 7
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPDelete(_AFPCommand):
    code = 8
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPEnumerate(_AFPCommand):
    code = 9
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPFlush(_AFPCommand):
    code = 10
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPFlushFork(_AFPCommand):
    code = 11
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPGetForkParms(_AFPCommand):
    code = 14
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPGetSrvrInfo(_AFPCommand):
    code = 15
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass


class FPGetSrvrParms(_AFPCommand):
    code = 16
    # Docs says there is a pad byte, but doesn't always seem to be there.
    _request = struct.Struct('!B')
    # Docs say the second field is int16, but it seems to be a single byte
    _response = struct.Struct('!iB')

    def request(self, data):
        return self._request.unpack(data[:self._request.size])

    def response(self, data):
        time, count = self._response.unpack(data[:self._response.size])
        data = data[self._response.size:]
        volumes = []

        for _ in range(count):
            flags = struct.unpack('!B', data[:1])[0]
            name, data = take_string(data[1:])
            volumes.append((flags, name))

        return afp_datetime(time), count, tuple(volumes)


class FPGetVolParms(_AFPCommand):
    code = 17
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPLogin(_AFPCommand):
    code = 18
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPLoginCont(_AFPCommand):
    code = 19
    _request = struct.Struct('!BBh')

    def request(self, data):
        command_code, pad, number = self._request.unpack(data[:self._request.size])
        return command_code, number, '+%d bytes' % len(data[self._request.size:])

    def response(self, data):
        pass



class FPLogout(_AFPCommand):
    code = 20
    # Docs say there is a pad byte. Sometimes there ain't.
    _request = struct.Struct('!B')

    def request(self, data):
        command_code = self._request.unpack(data[:self._request.size])[0]
        return (command_code,)

    def response(self, data):
        pass



class FPMapID(_AFPCommand):
    code = 21
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPMapName(_AFPCommand):
    code = 22
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPMoveAndRename(_AFPCommand):
    code = 23
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPOpenVol(_AFPCommand):
    code = 24
    _request = struct.Struct('!BBh')

    def request(self, data):
        command, pad, bitmap = self._request.unpack(data[:self._request.size])
        name, data = take_string(data[self._request.size:])
        return command, bitmap, name

    def response(self, data):
        pass



class FPOpenDir(_AFPCommand):
    code = 25
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPOpenFork(_AFPCommand):
    code = 26
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPRead(_AFPCommand):
    code = 27
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPRename(_AFPCommand):
    code = 28
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPSetDirParms(_AFPCommand):
    code = 29
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPSetFileParms(_AFPCommand):
    code = 30
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPSetForkParms(_AFPCommand):
    code = 31
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPSetVolParms(_AFPCommand):
    code = 32
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPWrite(_AFPCommand):
    code = 33
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPGetFileDirParms(_AFPCommand):
    code = 34
    _request = struct.Struct('!BBhihh')

    def request(self, data):
        parts = self._request.unpack(data[:self._request.size])
        return parts

    def response(self, data):
        pass



class FPSetFileDirParms(_AFPCommand):
    code = 35
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPChangePassword(_AFPCommand):
    code = 36
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPGetUserInfo(_AFPCommand):
    code = 37
    _request = struct.Struct('!BBih')

    def request(self, data):
        size = self._request.size
        command, flags, userid, bitmap = self._request.unpack(data[:size])
        return command, flags, userid, bitmap

    def response(self, data):
        pass



class FPGetSrvrMsg(_AFPCommand):
    code = 38
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPCreateId(_AFPCommand):
    code = 39
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPDeleteID(_AFPCommand):
    code = 40
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPResolveID(_AFPCommand):
    code = 41
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPExchangeFiles(_AFPCommand):
    code = 42
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPCatSearch(_AFPCommand):
    code = 43
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPOpenDT(_AFPCommand):
    code = 48
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPCloseDT(_AFPCommand):
    code = 49
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPGetIcon(_AFPCommand):
    code = 51
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPAddAPPL(_AFPCommand):
    code = 53
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPRemoveAPPL(_AFPCommand):
    code = 54
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPGetAPPL(_AFPCommand):
    code = 55
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPAddComment(_AFPCommand):
    code = 56
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPRemoveComment(_AFPCommand):
    code = 57
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPGetComment(_AFPCommand):
    code = 58
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPByteRangeLockExt(_AFPCommand):
    code = 59
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPReadExt(_AFPCommand):
    code = 60
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPWriteExt(_AFPCommand):
    code = 61
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPGetAuthMethods(_AFPCommand):
    code = 62
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPLoginExt(_AFPCommand):
    code = 63
    _request = struct.Struct('!BBh')

    def request(self, data):
        # Set everything to None at first.
        command_code = flags = version = uam = user = path = info = None

        start, data = data[:self._request.size], data[self._request.size:]
        command_code, pad, flags = self._request.unpack(start)

        assert data

        # Next is the ASCII version string. First byte is length.
        version_string, data = take_string(data)
        version = constants.afp_versions.get(version_string, version_string)

        # Next is the ASCII UAM string.First byte is length again.
        uam_string, data = take_string(data)
        uam = constants.afp_uams.get(uam_string, uam_string)

        logging.debug('data: %r', data)
        # Next is the user login name but it is always UTF-8 and the docs say
        # it is an AFPName but it is actually just 2 bytes for the length
        # followed by the string
        _, size = struct.unpack('!Bh', data[:3])
        data = data[3:]
        name = struct.unpack('!%ss' % size, data[:size])[0]
        data = data[size:]

        # Next is the Open Directory domain to search for the given username.
        path, data = take_name(data)

        # Next is the UAM info. May be a null byte. Or may be the padding to
        # put the UAM on an even byte. How do I know if a pad byte was needed?
        # For now we ignore UAM info.

        return (command_code, flags, version, uam, user, path, info)

    def response(self, data):
        pass



class FPGetSessionToken(_AFPCommand):
    code = 64
    _request = struct.Struct('!BBh')
    def request(self, data):
        command, pad, type_ = self._request.unpack(data[:self._request.size])
        return command, type_

    def response(self, data):
        pass



class FPDisconnectOldSession(_AFPCommand):
    code = 65
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPEnumerateExt(_AFPCommand):
    code = 66
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPCatSearchExt(_AFPCommand):
    code = 67
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass


class FPEnumerateExt2(_AFPCommand):
    """Lists the contents of a directory."""
    code = 68
    _request = struct.Struct('!BBhihhhii')
    _response = struct.Struct('!hhh')

    def request(self, data):
        parts = self._request.unpack(data[:self._request.size])
        (command, _, vol_id, dir_id, file_bitmap, dir_bitmap, req_count,
            start_index, max_reply_size) = parts
        name, data = take_name(data[self._request.size:])

        return (command, vol_id, dir_id, file_bitmap, dir_bitmap, req_count,
                start_index, max_reply_size, name)

    def response(self, data):
        file_bitmap, dir_bitmap, count = self._response.unpack(data[:self._response.size])
        return file_bitmap, dir_bitmap, count


class FPGetExtAttr(_AFPCommand):
    code = 69
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass


class FPSetExtAttr(_AFPCommand):
    code = 70
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPRemoveExtAttr(_AFPCommand):
    code = 71
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPListExtAttrs(_AFPCommand):
    code = 72
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPGetACL(_AFPCommand):
    code = 73
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPSetACL(_AFPCommand):
    code = 74
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPAccess(_AFPCommand):
    code = 75
    _request = struct.Struct('!BBhiH16si')
    def request(self, data):
        parts = self._request.unpack(data[:self._request.size])
        command, _, vol_id, dir_id, bitmap, uuid, access = parts
        path, data = take_name(data[self._request.size:])
        return (command, vol_id, dir_id, bitmap, uuid, access, path)

    def response(self, data):
        pass



class FPSpotlightRPC(_AFPCommand):
    code = 76
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPSyncDir(_AFPCommand):
    code = 78
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPSyncFork(_AFPCommand):
    code = 79
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPZzzzz(_AFPCommand):
    code = 122
    def request(self, data):
        return struct.unpack('!B', data[:1])

    def response(self, data):
        pass



class FPAddIcon(_AFPCommand):
    code = 192
    def request(self, data):
        return struct.unpack('!B', data[:1])

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
            name_type, byte2, byte3 = struct.unpack('!BBB', data[:3])
            # Zero-length names are just 2 null bytes.
            if byte2 == 0 and byte3 == 0:
                return '', data[:3]
        except struct.error:
            raise BadNameError

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

        # AFP uses null-bytes in the path name as a directory separator.
        name = parts[-1].replace(chr(0), ':')
        # Ummm, the name is either unicode or some crazy Mac encoding that depends
        # on the volume or client encoding. So you choose.
        return name, data[offset:]


take_name = AFPName()


def take_string(data):
    """Returns a string and the remaining data. The first byte is the size of
    the string.
    """
    count = struct.unpack('!B', data[:1])[0]
    fmt = struct.Struct('!B%ds' % count)
    count, name = fmt.unpack(data[:fmt.size])
    return name, data[fmt.size:]


#: AFP uses seconds since midnight 2000-01-01.
afp_epoch = datetime(2000, 1, 1, 0, 0, 0)


def afp_datetime(seconds):
    """Make a datetime from an AFP time value."""
    return afp_epoch + timedelta(seconds=seconds)


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


