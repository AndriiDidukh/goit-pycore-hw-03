import re


def normalize_phone(phone_number):
    normalized_number = re.sub(r'[^\d+]', '', phone_number)

    if not normalized_number.startswith('+'):
        if normalized_number.startswith('380'):
            normalized_number = '+' + normalized_number
        else:
            normalized_number = '+38' + normalized_number
    elif normalized_number.startswith('+') and not normalized_number.startswith('+38'):
        if normalized_number.startswith('+380'):
            pass
        else:
            normalized_number = '+38' + normalized_number[1:]

    return normalized_number


print(normalize_phone('097 777 77 77'))
print(normalize_phone('+38(097)7777777'))
print(normalize_phone('380977777777'))