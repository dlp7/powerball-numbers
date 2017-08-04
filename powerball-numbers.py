from collections import Counter, namedtuple
import random

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
    powerball_ticket = []

    for i in range(6):
        # Generate counts, excluding any that are already picked if first five numbers.
        if i < 5:
            counts = Counter([entry.numbers[i] for entry in entries if entry.numbers[i] not in powerball_ticket])
        else:
            counts = Counter([entry.numbers[i] for entry in entries])
        # Count of most common occurrence, most_common returns list of (val, count) tuples up to parameter given (1).
        max_count = counts.most_common(1)[0][1]
        # Get most common values as candidates for ticket
        candidates = [x[0] for x in counts.most_common() if x[1] == max_count]

        # Pick random from candidates. If only 1 candidate, that will be returned.
        powerball_ticket.append(random.choice(candidates))

    return powerball_ticket


def non_empty_prompt(prompt):
    while True:
        val = input(prompt).strip()
        if val:
            break
        print('Empty input is not allowed.')

    return val


def new_entry():
    # TODO: Prompt for name, numbers
    firstname = non_empty_prompt('Please enter your first name: ')
    lastname = non_empty_prompt('Please enter your last name: ')
    name = '{} {}'.format(firstname, lastname)

    numbers = []
    # Prompt for 5 numbers
    for i in range(5):
        prompt_for_favorite(numbers)

    powerball = prompt_for_powerball()
    numbers.append(powerball)

    return Entry(name=name, numbers=numbers)


if __name__ == '__main__':
    # TODO: Define main loop
    pass
