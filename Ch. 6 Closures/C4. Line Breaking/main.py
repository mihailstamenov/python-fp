from functools import reduce


def lineator(line_length):
    def lineate(document):
        words = document.split()

        def add_word_to_lines(lines, word):
            pass

        return reduce(add_word_to_lines, words, [])

    return lineate
