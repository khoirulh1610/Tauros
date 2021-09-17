import Crypto as crypto
import re
r = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70]
a = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 97, 98, 99, 100, 101, 102]

StringFromCharCode = lambda x: ''.join(map(chr, x)) # Python evivalent of String.fromCharCode.apply(String, x)
StringCharCodeAt = lambda x, i: ord(x[i])
def i (e):
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
    else: return 10 + r - 97

def s(e):
    if re.match("[^0-9a-fA-F]", e):
        raise ValueError(f"{e} is not a valid hex")
    return e
