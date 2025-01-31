def sort_dates(dates):
    return sorted(dates, key=transform)

def transform(date):
    return f"{date[6:]}-{date[0:2]}-{date[3:5]}"