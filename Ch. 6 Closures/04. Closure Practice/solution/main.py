def new_collection(initial_docs):
    cp = initial_docs[:]
    def appender(str):
        cp.append(str)
        return cp
    return appender