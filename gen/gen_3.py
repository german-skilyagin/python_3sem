from datetime import datetime, timedelta

def generate_dow(month, day, year):
    current_date = datetime(year, month, day)
    while True:
        yield current_date.strftime("%A")
        current_date += timedelta(days=1)

for dow in generate_dow(10, 11, 2020):
    print(dow)
    if dow == "Monday":
        break
