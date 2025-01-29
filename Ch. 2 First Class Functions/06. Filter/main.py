def remove_invalid_lines(document):
    split = document.split("\n")
    filtered = list(filter(lambda x: x.startswith("*"), split))
    res = "\n".join(filtered)
    return f"\n{res}\n"