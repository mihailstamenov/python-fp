def word_count_memo(document, memos):
    memos_cp = memos.copy()
    if document in memos_cp:
        return (memos_cp[document], memos_cp)
    memos_cp[document] = word_count(document)
    return (word_count(document), memos_cp)

# Don't edit below this line


def word_count(document):
    count = len(document.split())
    return count
