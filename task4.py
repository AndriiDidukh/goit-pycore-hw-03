from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    end_date = today + timedelta(days=7)

    for user in users:
        name = user['name']
        birthday_str = user['birthday']
        birthday = datetime.strptime(birthday_str, '%Y.%m.%d').date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        if today <= birthday_this_year <= end_date:
            if birthday_this_year.weekday() in (5, 6):
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

            upcoming_birthdays.append({
                'name': name,
                'congratulation_date': birthday_this_year.strftime('%Y.%m.%d')
            })

    return upcoming_birthdays


users = [
    {'name': 'Andrii', 'birthday': '1985.07.14'},
    {'name': 'Ivan', 'birthday': '1992.07.21'},
]

print(get_upcoming_birthdays(users))