def pair_document_with_format(doc_names, doc_formats):
    res = list(zip(doc_names, doc_formats))
    final = filter(lambda x: x[1] in valid_formats, res)
    return list(final)