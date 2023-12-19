import random

from settings import CHARACTERS, LENGTH_SHORT_LINK


def check_custom_id(custom_id):
    for character in custom_id:
        if character not in CHARACTERS:
            return False
    return len(custom_id) <= LENGTH_SHORT_LINK


def get_unique_short_id():
    short_link = ''.join(random.choice(CHARACTERS) for character in range(6))
    return short_link
