import datetime
day = int(input("Input day: "))
month = int(input("Input month: "))
year = int(input("Input year: "))


def is_date(some_year, some_month, some_day):
    try:
        datetime.date(some_year, some_month, some_day)
        return True
    except:
        return False


print(is_date(year, month, day))