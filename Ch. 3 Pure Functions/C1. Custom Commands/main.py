default_commands = {}
default_formats = ["txt", "md", "html"]
saved_documents = {}

# Don't edit above this line


def add_custom_command(commands, new_command, function):
    commands[new_command] = function
    return commands


def add_format(formats, format):
    formats.append(format)
    return formats


def save_document(docs, file_name, doc):
    docs[file_name] = doc
    return docs


def add_line_break(line):
    print(line + "\n\n")
