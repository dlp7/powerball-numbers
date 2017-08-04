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


def prompt_for_favorite(numbers):
    # TODO: Define loop to prompt for number, check against type, range, and existing.
    minval = 1
    maxval = 69

    indexes = {0: '1st', 1: '2nd', 2: '3rd', 3: '4th', 4: '5th', 5: '6th'}
    index = indexes[len(numbers)]

    excludingtext = ''
    if len(numbers) == 1:
        excludingtext = ' excluding {}'.format(numbers[0])
    elif len(numbers) == 2:
        excludingtext = ' excluding {} and {}'.format(numbers[0], numbers[-1])
    elif len(numbers) > 2:
        excludingtext = ' excluding {}, and {}'.format(', '.join(map(str, numbers[:-1])), numbers[-1])

    prompt = 'select {} # ({} thru {}{}): '.format(index, minval, maxval, excludingtext)

    while True:
        num = prompt_for_number(prompt, minval, maxval)
        if num in numbers:
            print('{} has already been picked.'.format(num))
        else:
            break

    numbers.append(num)


def prompt_for_powerball():
    minval = 1
    maxval = 26
    prompt = 'select Power Ball # ({} thru {}): '.format(minval, maxval)
    return prompt_for_number(prompt, minval, maxval)


def create_ticket(entries):
    # TODO: Loop entries
    pass


def new_entry():
    # TODO: Prompt for name, numbers
    pass


if __name__ == '__main__':
    # TODO: Define main loop
    pass
