"""Challenge 00
Given a string `S`.
Convert `S` to sequence of bytes object then get its length.

    Remarks
Python3 has two types of object representing a string. First is `str` which represent
sequence of characters, other is `bytes` which represent sequence of bytes. Both are immutable string.
The `str` object represent string as multibyte string, which supports unicode.
In other hand, `bytes` represent single byte character.
In most case, string in Python refer to the string of `str` type.
In some cases, we need to operate on low level data which are sequence of bytes.
Thus, converting string to sequence of byte is desirable.
When you will see and use bytes?
- crafting shellcode (payload).
- send/receive data on socket.
- analyze value of memory addresses.
- dump data from disk.
"""

s: str = "memory"


def convert_string_to_bytes_object(s: str) -> bytes:
    return s.encode()


string_to_byte = convert_string_to_bytes_object("memory")

print(s)
print(string_to_byte)
print(type(string_to_byte))
