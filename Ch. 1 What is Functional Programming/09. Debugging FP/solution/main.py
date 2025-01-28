def format_line(line):
    stripped = line.strip()
    capitalized = stripped.upper()
    rm_punc = capitalized.replace(".", "")
    suffixed = f"{rm_punc}..."
    return suffixed
