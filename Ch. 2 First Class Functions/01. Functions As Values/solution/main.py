def file_to_prompt(file, to_string):
    stringified = to_string(file)
    return f"```\n{stringified}\n```"

# def file_to_prompt(file, to_string):
#     return f"```\n{to_string(file)}\n```"
