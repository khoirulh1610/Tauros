from typing import cast
import Cryptodome as crypto
import re
import os
r = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70]
a = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 97, 98, 99, 100, 101, 102]

StringFromCharCode = lambda x: "".join(
    map(chr, x)
)  # Python evivalent of String.fromCharCode.apply(String, x)
StringCharCodeAt = lambda x, i: ord(x[i])


def i(e):
    t = []
    for a in e:
        t.append(r[a >> 4])
        t.append(r[15 & a])

    return StringFromCharCode(t)


def n(e, t):
    r = StringCharCodeAt(e, t)
    if r <= 57:
        return r - 48
    elif r <= 70:
        return 10 + r - 65
    else:
        return 10 + r - 97


def s(e):
    if re.match("[^0-9a-fA-F]", e):
        raise ValueError(f"{e} is not a valid hex")
    return e


def o(e, t):
    # convert all elemts of array to str python
    n = [str(_) for _ in e]
    return (t - len(e)) * "0" + ",".join(n)


def l(e):
    return e[0] == "-"


def d(e):
    if e > 4294967295 or e < -4294967296:
        raise ValueError(f"uint32ToLowerCaseHex given number over 32 bits")
    return o(e if e >= 0 else (4294967296 + e), 8)


NUM_HEX_IN_LONG = 16
HEX_LOWER = a


def randomHex(length):
    return i(os.urandom(length))


toHex = i

def toLowerCaseHex(e):
    t = []
    for r in e:
        t.append(a[r >> 4])
        t.append(a[15 & r])

    return StringFromCharCode(t)


def parseHex(e):
    t = s(e)
    if(len(t) % 2 != 0):
        raise ValueError(f"{e} is not a valid hex")
    r = bytearray((len(t) >> 1))
    a = 0
    i = 0
    for a in range(a, len(t)-2, 2):
        i += 1
        r[i] = (n(t, a) << 4) | n(t, a+1)
    return r

hexAt = n
hexOrThrow = s

def bytesToDebugString(e):
    t = True
    r = len(e)
    a = e[r-1]
    t = 32 <= a and a < 127
    
    if t : return str(StringFromCharCode(e))
    else : return i(e)

def hexLongToHex(e : str):
    try:
        index = e.index("0x")
    except:
        index = 0
    return e[index+2:]

hexLongIsNegative = l;

def negateHexLong(e):
    if l(e): return e[1:]
    else: return f"-{e}"