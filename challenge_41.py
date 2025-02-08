"""Calculate days between two dates"""
from datetime import datetime


first_date: datetime = datetime(2025, 1, 1)
second_date: datetime = datetime(2025, 2, 28)


def calculate_days_between_dates(first_date: datetime, second_date: datetime):
    return (second_date - first_date).days


if __name__ == "__main__":
    result: datetime = calculate_days_between_dates(first_date=first_date, second_date=second_date)
    print(result)
