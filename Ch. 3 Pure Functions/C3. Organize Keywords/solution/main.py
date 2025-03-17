def map_keywords(document, document_map):
    new_document_map = document_map.copy()
    if document in new_document_map:
        return new_document_map[document], new_document_map
    found_keywords = find_keywords(document)
    new_document_map[document] = found_keywords
    return found_keywords, new_document_map


def find_keywords(document):
    keywords = [
        "functional",
        "immutable",
        "declarative",
        "higher-order",
        "lambda",
        "deterministic",
        "side-effects",
        "memoization",
        "referential transparency",
    ]
    lowered_doc = document.lower()
    return list(filter(lambda keyword: keyword in lowered_doc, keywords))
