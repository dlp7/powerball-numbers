from collections import namedtuple

Entry = namedtuple('Entry', ['name', 'numbers'])


def is_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def prompt_for_number(prompttext, minval, maxval):
    while True:
        answertext = input(prompttext)
        if is_number(answertext) and minval <= int(answertext) <= maxval:
            break
        print('Please enter a number within {} and {}.'.format(minval, maxval))

    return int(answertext)


def prompt_for_favorite(person, numbers=None):
    # TODO: Define loop to prompt for number, check against type, range, and existing.
    pass


def prompt_for_powerball(person, numbers):
    # TODO: Define loop to prompt for number, check against type and range.
    pass


def create_ticket(entries):
    # TODO: Loop entries
    pass


def new_entry():
    # TODO: Prompt for name, numbers
    pass


if __name__ == '__main__':
    # TODO: Define main loop
    pass
