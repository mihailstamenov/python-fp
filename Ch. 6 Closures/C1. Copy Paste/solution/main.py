def new_clipboard(initial_clipboard):
    clipboard = initial_clipboard.copy()

    def copy_to_clipboard(key, value):
        clipboard[key] = value

    def paste_from_clipboard(key):
        if key in clipboard:
            return clipboard[key]
        return ""

    return copy_to_clipboard, paste_from_clipboard
