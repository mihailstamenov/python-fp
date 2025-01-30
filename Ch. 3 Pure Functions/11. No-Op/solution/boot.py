def remove_emphasis_from_word(word):
    return word.strip("*")


def remove_emphasis_from_line(line):
    words = line.split()
    new_words = map(remove_emphasis_from_word, words)
    return " ".join(new_words)


def remove_emphasis(doc_content):
    lines = doc_content.split("\n")
    new_lines = map(remove_emphasis_from_line, lines)
    return "\n".join(new_lines)
