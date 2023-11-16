from datetime import datetime, timedelta

def generate_dates(month, day, year):
    current_date = datetime(year, month, day)
    while True:
        yield current_date
        current_date += timedelta(days=1)

for date in generate_dates(9, 1, 2022):
    print(date.strftime("%d.%m.%Y"))
    if date.year > 2022 or (date.year == 2022 and date.month > 12):
        break