"""Challenge 05
Given a string of a hexpair `H`.Decode (or convert) `H` as a sequence of bytes.
The content might or might not be printable characters.
The length of `H` is guaranteed to be even.
    Test
The hexpair string `H` (length = 24) -> 526576657273696e672e4944
should be converted to (length = 12) -> \x52\x65\x76\x65\x72\x73\x69\x6e\x67\x2e\x49\x44
    Remarks
Representing binary data in hexpair string is not unusual. Although some encoding such as Base64
is more popular. Hex pairs are often found on low level stuffs for representing stream of data.
"""


hexpair: str = "526576657273696e672e4944"


def hexpair_converted_with_recursivity(hexpair: str, begin: str = "") -> str:
    begin += f"\\x{[hexpair][0][0]}{[hexpair][0][1]}"
    if len(hexpair[2:]) > 0:
        return hexpair_converted_with_recursivity(hexpair[2:], begin)
    return begin


def hexpair_converted(hexpair: str) -> str:
    return "".join(
        ["\\x"+hexpair[i:i+2] for i in range(0, len(hexpair), 2)]
    )



print(hexpair_converted(hexpair))
print(hexpair_converted_with_recursivity(hexpair))
