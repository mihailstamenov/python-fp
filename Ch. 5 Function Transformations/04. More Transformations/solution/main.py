def doc_format_checker_and_converter(conversion_function, valid_formats):
    def inner_converter(filename, content):
        file_extension = filename.split(".")[-1]
        if file_extension in valid_formats:
            return conversion_function(content)
        raise ValueError("invalid file format")

    return inner_converter


# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]
