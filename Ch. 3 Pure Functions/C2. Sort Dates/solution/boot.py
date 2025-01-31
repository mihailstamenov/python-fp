def sort_dates(dates):
    return sorted(dates, key=format_date)


def format_date(date):
    month, day, year = date.split("-")
    return year + month + day
