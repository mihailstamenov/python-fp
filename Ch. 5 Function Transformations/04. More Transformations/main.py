def doc_format_checker_and_converter(conversion_function, valid_formats):
    def func(filename, content):
        format = filename.split('.', maxsplit=1)
        if format[1] in valid_formats:
            return conversion_function(content)
        else: raise ValueError("invalid file format")
    return func


# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]
