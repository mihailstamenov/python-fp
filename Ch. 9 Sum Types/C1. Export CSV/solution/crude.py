from enum import Enum


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


def get_csv_status(status, data):
    match status:
        case CSVExportStatus.PENDING:
            return ("Pending...", list(map(lambda s: list(map(str, s)), data)))
        case CSVExportStatus.PROCESSING:
            return ("Processing...", "\n".join(list(map(lambda s: ",".join(s), data))))
        case CSVExportStatus.SUCCESS:
            return ("Success!",data)
        case CSVExportStatus.FAILURE:
            to_strings = list(map(lambda s: list(map(str, s)), data))
            to_csv = "\n".join(list(map(lambda s: ",".join(s), to_strings)))
            return ("Unknown error, retrying...", to_csv)
        case _:
            raise Exception("unknown export status")
