from datetime import datetime


def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return "Incorect data value. Please use '%Y-%m-%d'."
    today = datetime.today().date()
    delta = today - given_date
    return delta.days


print(get_days_from_today('2024-07-14'))
