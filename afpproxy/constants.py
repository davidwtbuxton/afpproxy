# -*- coding: utf-8 -*-
# DSI commands
kDSICloseSession = 1
kDSICommand = 2
kDSIGetStatus = 3
kDSIOpenSession = 4
kDSITickle = 5
kDSIWrite = 6
kDSIAttention = 8

# Codes for AFPName structures.
kFPShortName = 1
kFPLongName = 2
kFPUTF8Name = 3

# AFP version strings, used in FPLogin
afp_versions = {
    'AFPVersion 2.1': 'kAFPVersion_2_1',
    'AFP2.2': 'kAFPVersion_2_2',
    'AFP2.3': 'kAFPVersion_2_3',
    'AFPX03': 'kAFPVersion_3_0',
    'AFP3.1': 'kAFPVersion_3_1',
    'AFP3.2': 'kAFPVersion_3_2',
    'AFP3.3': 'kAFPVersion_3_3',
}

# AFP UAM strings, used in FPLogin/FPLoginExt
afp_uams = {
    'No User Authent': 'kNoUserAuthStr',
    'Cleartxt Passwrd': 'kClearTextUAMStr',
    'Randnum Exchange': 'kRandNumUAMStr',
    '2-Way Randnum': 'kTwoWayRandNumUAMStr',
    'DHCAST128': 'kDHCAST128UAMStr',
    'DHX2': 'kDHX2UAMStr',
    'Client Krb v2': 'kKerberosUAMStr',
    'Recon1': 'kReconnectUAMStr',
}

# AFP text encodings
encodings = {
    0: 'kTextEncodingMacRoman',
    1: 'kTextEncodingMacJapanese',
    2: 'kTextEncodingMacChineseTrad',
    3: 'kTextEncodingMacKorean',
    4: 'kTextEncodingMacArabic',
    5: 'kTextEncodingMacHebrew',
    6: 'kTextEncodingMacGreek',
    7: 'kTextEncodingMacCyrillic',
    9: 'kTextEncodingMacDevanagari',
    10: 'kTextEncodingMacGurmukhi',
    11: 'kTextEncodingMacGujarati',
    12: 'kTextEncodingMacOriya',
    13: 'kTextEncodingMacBengali',
    14: 'kTextEncodingMacTamil',
    15: 'kTextEncodingMacTelugu',
    16: 'kTextEncodingMacKannada',
    17: 'kTextEncodingMacMalayalam',
    18: 'kTextEncodingMacSinhalese',
    19: 'kTextEncodingMacBurmese',
    20: 'kTextEncodingMacKhmer',
    21: 'kTextEncodingMacThai',
    22: 'kTextEncodingMacLaotian',
    23: 'kTextEncodingMacGeorgian',
    24: 'kTextEncodingMacArmenian',
    25: 'kTextEncodingMacChineseSimp',
    26: 'kTextEncodingMacTibetan',
    27: 'kTextEncodingMacMongolian',
    28: 'kTextEncodingMacEthiopic',
    29: 'kTextEncodingMacCentralEurRoman',
    30: 'kTextEncodingMacVietnamese',
    31: 'kTextEncodingMacExtArabic',
    33: 'kTextEncodingMacSymbol',
    34: 'kTextEncodingMacDingbats',
    35: 'kTextEncodingMacTurkish',
    36: 'kTextEncodingMacCroatian',
    37: 'kTextEncodingMacIcelandic',
    38: 'kTextEncodingMacRomanian',
    39: 'kTextEncodingMacCeltic',
    40: 'kTextEncodingMacGaelic',
    41: 'kTextEncodingMacKeyboardGlyphs',
    126: 'kTextEncodingMacUnicode',
    140: 'kTextEncodingMacFarsi',
    152: 'kTextEncodingMacUkrainian',
    236: 'kTextEncodingMacInuit',
    252: 'kTextEncodingMacVT100',
    255: 'kTextEncodingMacHFS',
    256: 'kTextEncodingUnicodeDefault',
    257: 'kTextEncodingUnicodeV1_1',
    257: 'kTextEncodingISO10646_1993',
    259: 'kTextEncodingUnicodeV2_0',
    259: 'kTextEncodingUnicodeV2_1',
    260: 'kTextEncodingUnicodeV3_0',
    513: 'kTextEncodingISOLatin1',
    514: 'kTextEncodingISOLatin2',
    515: 'kTextEncodingISOLatin3',
    516: 'kTextEncodingISOLatin4',
    517: 'kTextEncodingISOLatinCyrillic',
    518: 'kTextEncodingISOLatinArabic',
    519: 'kTextEncodingISOLatinGreek',
    520: 'kTextEncodingISOLatinHebrew',
    521: 'kTextEncodingISOLatin5',
    522: 'kTextEncodingISOLatin6',
    525: 'kTextEncodingISOLatin7',
    526: 'kTextEncodingISOLatin8',
    527: 'kTextEncodingISOLatin9',
    1024: 'kTextEncodingDOSLatinUS',
    1029: 'kTextEncodingDOSGreek',
    1030: 'kTextEncodingDOSBalticRim',
    1040: 'kTextEncodingDOSLatin1',
    1041: 'kTextEncodingDOSGreek1',
    1042: 'kTextEncodingDOSLatin2',
    1043: 'kTextEncodingDOSCyrillic',
    1044: 'kTextEncodingDOSTurkish',
    1045: 'kTextEncodingDOSPortuguese',
    1046: 'kTextEncodingDOSIcelandic',
    1047: 'kTextEncodingDOSHebrew',
    1048: 'kTextEncodingDOSCanadianFrench',
    1049: 'kTextEncodingDOSArabic',
    1050: 'kTextEncodingDOSNordic',
    1051: 'kTextEncodingDOSRussian',
    1052: 'kTextEncodingDOSGreek2',
    1053: 'kTextEncodingDOSThai',
    1056: 'kTextEncodingDOSJapanese',
    1057: 'kTextEncodingDOSChineseSimplif',
    1058: 'kTextEncodingDOSKorean',
    1059: 'kTextEncodingDOSChineseTrad',
    1280: 'kTextEncodingWindowsLatin1',
    1280: 'kTextEncodingWindowsANSI',
    1281: 'kTextEncodingWindowsLatin2',
    1282: 'kTextEncodingWindowsCyrillic',
    1283: 'kTextEncodingWindowsGreek',
    1284: 'kTextEncodingWindowsLatin5',
    1285: 'kTextEncodingWindowsHebrew',
    1286: 'kTextEncodingWindowsArabic',
    1287: 'kTextEncodingWindowsBalticRim',
    1288: 'kTextEncodingWindowsVietnamese',
    1296: 'kTextEncodingWindowsKoreanJohab',
    1536: 'kTextEncodingUS_ASCII',
    1568: 'kTextEncodingJIS_X0201_76',
    1569: 'kTextEncodingJIS_X0208_83',
    1570: 'kTextEncodingJIS_X0208_90',
}

# AFP error response codes. These go in the offset/error field of the DSI header.
errors = {
    0: 'kFPNoErr',	# No error (success).
    -1068: 'kFPNoMoreSessions',	# Server cannot handle additional sessions.# This error usually indicates that the server limits the maximum number of concurrent clients, and that this maximum number would be exceeded by honoring this login request.
    -1072: 'kASPSessClosed',	# ASP session closed.
    -5000: 'kFPAccessDenied',	# User does not have the access privileges required to use the command.
    -5001: 'kFPAuthContinue',	# Authentication is not yet complete.
    -5002: 'kFPBadUAM',	# Specified UAM is unknown
    -5003: 'kFPBadVersNum',	# Server does not support the specified AFP version.
    -5004: 'kFPBitmapErr',	# Attempt was made to get or set a parameter that cannot be obtained or set with this command, or a required bitmap is null
    -5005: 'kFPCantMove',	# Attempt was made to move a directory into one of its descendent directories.
    -5006: 'kFPDenyConflict',	# Specified fork cannot be opened because of a deny modes conflict.
    -5007: 'kFPDirNotEmpty',	# Directory is not empty.
    -5008: 'kFPDiskFull',	# No more space exists on the volume
    -5009: 'kFPEOFErr',	# No more matches or end of fork reached.
    -5010: 'kFPFileBusy',	# When attempting a hard create, the file already exists and is open.
    -5011: 'kFPFlatVol',	# Volume is flat and does not support directories.
    -5012: 'kFPItemNotFound',	# Specified APPL mapping, comment, or icon was not found in the Desktop database; specified ID is unknown.# Beginning in AFP 3.4, the POSIX error code ENOATTR maps onto this error code. In prior AFP versions, the ENOATTR error was mapped on to the “kFPMiscErr” error code.
    -5013: 'kFPLockErr',	# Some or all of the requested range is locked by another user; a lock range conflict exists.
    -5014: 'kFPMiscErr',	# Non-AFP error occurred.
    -5015: 'kFPNoMoreLocks',	# Server’s maximum lock count has been reached.
    -5016: 'kFPNoServer',	# Server is not responding.
    -5017: 'kFPObjectExists',	# File or directory already exists.
    -5018: 'kFPObjectNotFound',	# Input parameters do not point to an existing directory, file, or volume.
    -5019: 'kFPParamErr',	# Session reference number, Desktop database reference number, open fork reference number, Volume ID, Directory ID, File ID, Group ID, or subfunction is unknown; byte range starts before byte zero; pathname is invalid; pathname type is unknown; user name is null, exceeds the UAM’s user name length limit, or does not exist, MaxReplySize is too small to hold a single offspring structure, ThisUser bit is not set, authentication failed for an undisclosed reason, specified user is unknown or the account has been disabled due to too many login attempts; ReqCount or Offset is negative; NewLineMask is invalid.
    -5020: 'kFPRangeNotLocked',	# Attempt to unlock a range that is locked by another user or that is not locked at all.
    -5021: 'kFPRangeOverlap',	# User tried to lock some or all of a range that the user has already locked.
    -5022: 'kFPSessClosed',	# Session is closed.
    -5023: 'kFPUserNotAuth',	# UAM failed (the specified old password doesn’t match); no user is logged in yet for the specified session; authentication failed; password is incorrect.
    -5024: 'kFPCallNotSupported',	# Server does not support this command.
    -5025: 'kFPObjectTypeErr',	# Input parameters point to the wrong type of object.
    -5026: 'kFPTooManyFilesOpen',	# Server cannot open another fork.
    -5027: 'kFPServerGoingDown',	# Server is shutting down.
    -5028: 'kFPCantRename',	# Attempt was made to rename a volume or root directory.
    -5029: 'kFPDirNotFound',	# Input parameters do not point to an existing directory.
    -5030: 'kFPIconTypeError',	# New icon’s size is different from the size of the existing icon.
    -5031: 'kFPVolLocked',	# Volume is Read Only.
    -5032: 'kFPObjectLocked',	# File or directory is marked DeleteInhibit; directory being moved, renamed, or moved and renamed is marked RenameInhibit; file being moved and renamed is marked RenameInhibit; attempt was made to open a file for writing that is marked WriteInhibit; attempt was made to rename a file or directory that is marked RenameInhibit.
    -5033: 'kFPContainsSharedErr',	# Directory contains a share point.
    -5034: 'kFPIDNotFound',	# File ID was not found. (No file thread exists.)
    -5035: 'kFPIDExists',	# File already has a File ID.
    -5036: 'kFPDiffVolErr',	# Wrong volume.
    -5037: 'kFPCatalogChanged',	# Catalog has changed.
    -5038: 'kFPSameObjectErr',	# Two objects that should be different are the same object.
    -5039: 'kFPBadIDErr',	# File ID is not valid.
    -5040: 'kFPPwdSameErr',	# User attempted to change his or her password to the same password that is currently set.
    -5041: 'kFPPwdTooShortErr',	# User password is shorter than the server’s minimum password length, or user attempted to change password to a password that is shorter than the server’s minimum password length.
    -5042: 'kFPPwdExpiredErr',	# User’s password has expired.
    -5043: 'kFPInsideSharedErr',	# Directory being moved contains a share point and is being moved into a directory that is shared or is the descendent of a directory that is shared.
    -5044: 'kFPInsideTrashErr',	# Shared directory is being moved into the Trash; a directory is being moved to the trash and it contains a shared folder.
    -5045: 'kFPPwdNeedsChangeErr',	# User’s password needs to be changed.
    -5046: 'kFPPwdPolicyErr',	# New password does not conform to the server’s password policy.
    -5047: 'kFPDiskQuotaExceeded',	# Disk quota exceeded.
}
