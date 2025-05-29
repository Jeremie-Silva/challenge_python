"""Recreate an alternative to replace built-in function"""


sentence: str = "Mon nom est Bond, James Bond."



def replace_content(text: str, new_word: str, old_word: str) -> str:
    while old_word in text:
        begin: int = text.index(old_word)
        end: int = len(old_word) + begin
        _text = list(text)
        _text[begin:end] = list(new_word)
        text = "".join(_text)
    return text



if __name__ == "__main__":
    print(replace_content(sentence, "Tuche", "Bond"))
