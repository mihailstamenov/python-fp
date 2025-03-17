def new_collection(initial_docs):
    cp = initial_docs[:]
    def appender(str):
        cp.append(str)
        return cp
    return appender

# def new_collection(initial_docs):
#     docs = initial_docs.copy()

#     def add_doc(doc):
#         docs.append(doc)
#         return docs

#     return add_doc
