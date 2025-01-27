"""Sort a list alphabetically and divide it into 2 in the middle of the alphabet"""


first_half_alphabet: list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
second_half_alphabet: list[str] = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
words: list[str] = ["Pierre", "Marie", "Julien", "Astrid", "Zoé"]


def sort_and_split_in_two(words: list[str]) -> tuple[list[str], list[str]]:
    first_half_results: list[str] = []
    second_half_results: list[str] = []
    for word in sorted(words):
        if word[0].lower() in first_half_alphabet:
            first_half_results.append(word)
        if word[0].lower() in second_half_alphabet:
            second_half_results.append(word)
    return first_half_results, second_half_results


if __name__ == "__main__":
    first_half_results, second_half_results = sort_and_split_in_two(words=words)
    print(first_half_results)
    print(second_half_results)
