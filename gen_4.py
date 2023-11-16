import datetime

def generate_dates(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += datetime.timedelta(days=1)

def generate_dow(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date.strftime('%A')
        current_date += datetime.timedelta(days=1)

def generate_tuples(start_date, end_date):
    dates = generate_dates(start_date, end_date)
    dows = generate_dow(start_date, end_date)
    for date, dow in zip(dates, dows):
        yield (date.day, date.month, date.year, dow)

start_date = datetime.date(2021, 1, 1)
end_date = datetime.date(2021, 1, 10)

for date_tuple in generate_tuples(start_date, end_date):
    print(date_tuple)