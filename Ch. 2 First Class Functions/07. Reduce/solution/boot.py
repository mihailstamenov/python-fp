import functools


def join(doc_so_far, sentence):
    return doc_so_far + ". " + sentence


def join_first_sentences(sentences, n):
    if n == 0:
        return ""
    return functools.reduce(join, sentences[:n]) + "."
