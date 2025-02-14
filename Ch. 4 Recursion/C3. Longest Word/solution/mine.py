def find_longest_word(document, longest_word=""):
    if len(document) == 0:
        return longest_word
    split = document.split(' ', maxsplit=1)
    if len(split[0]) > len(longest_word):
        longest_word = split[0]
    res = find_longest_word(' '.join(split)[1:], longest_word)
    return res