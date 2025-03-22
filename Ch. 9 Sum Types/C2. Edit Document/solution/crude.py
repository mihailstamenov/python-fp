from enum import Enum


class EditType(Enum):
    NEWLINE = 1
    SUBSTITUTE = 2
    INSERT = 3
    DELETE = 4


def handle_edit(document, edit_type, edit):
    listed = document.split("\n")
    match edit_type:
        case EditType.NEWLINE:
            listed[edit["line_number"]] += "\n"
            return "\n".join(listed)
        case EditType.SUBSTITUTE:
            subst = listed[edit["line_number"]]
            listed[edit["line_number"]] = f"{subst[:edit['start']]}{edit['insert_text']}{subst[edit['end']:]}"
            return "\n".join(listed)
        case EditType.INSERT:
            insert = listed[edit["line_number"]]
            listed[edit["line_number"]] = f"{insert[edit['start']:]}{edit['insert_text']}"
            return "\n".join(listed)
        case EditType.DELETE:
            delete = listed[edit["line_number"]]
            listed[edit["line_number"]] = f"{delete[:edit['start']]}{delete[edit['end']:]}"
            return "\n".join(listed)
        case _:
            raise Exception("unknown edit type")
