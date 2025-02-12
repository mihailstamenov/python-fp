def count_nested_levels(nested_documents, target_document_id, level=1):
    for id in nested_documents:
        if id == target_document_id:
            return level
        res = count_nested_levels(nested_documents[id], target_document_id, level+1)
        if res != 1: return res
    return -1
