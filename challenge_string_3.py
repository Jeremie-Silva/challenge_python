"""Challenge 02
Given a string D and two integers S and E.
Rewrite the content of string, starts from index S to index E, fill with x.
The resulting string and D should have same length.
Also, try the same thing with bytes type.
    Test
Given a string D MII CyberSec Consulting Service and two integers S = 4 and E = 11.
the result should be :
MII xxxxxxxx Consulting Service

    Remarks
Index is a number to refer position of specific element.
String str and bytes are both immutable and do not support item assignment on their element.
Modify a string at certain range is not limited to masking. We can modify content of (structured) packets,
and create a rule: where and what to replace.
"""


text: str = "MII CyberSec Consulting Service"
begin: int = 4
end: int = 15
new_character = "x"


def replace_characters_in_text(text: str, begin: int, end: int, new_character: str) -> str:
    new_text = ""
    count = 1
    for letter in text:
        if letter == " ":
            new_text += " "
        elif begin <= count <= end:
            new_text += new_character
            count += 1
        else:
            new_text += letter
            count += 1
    return new_text


new_text = replace_characters_in_text(text, begin, end, new_character)

print(new_text)
print(len(text))
print(len(new_text))
