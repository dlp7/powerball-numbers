from collections import Counter, namedtuple
import random

Entry = namedtuple('Entry', ['name', 'numbers'])


def is_number(value):
    """
    Tests if the given object can be converted to a number.
    :param value: object to test
    :return: true if can be converted to a number, false if not
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def prompt_for_number(prompt, min_val, max_val):
    """
    Prompts user for a number within a specific range.
    :param prompt: text to display to user
    :param min_val: minimum accepted value (inclusive)
    :param max_val: maximum accepted value (inclusive)
    :return: entered number
    """
    while True:
        answer_text = input(prompt)
        if is_number(answer_text) and min_val <= int(answer_text) <= max_val:
            break
        print('Please enter a number within {} and {}.'.format(min_val, max_val))

    return int(answer_text)


def prompt_for_favorite(numbers):
    """
    Prompts user for their 5 favorite number, enforcing the number is in accepted
    range and not already entered. Number is added to the passed in list.
    :param numbers: previously given numbers
    :return: None
    """
    min_val = 1
    max_val = 69

    # Lookup for prompt of # in pretty format
    indexes = {0: '1st', 1: '2nd', 2: '3rd', 3: '4th', 4: '5th'}
    index = indexes[len(numbers)]

    # Generate readable format of what can't be entered
    excluding_text = ''
    if len(numbers) == 1:
        excluding_text = ' excluding {}'.format(numbers[0])
    elif len(numbers) == 2:
        excluding_text = ' excluding {} and {}'.format(numbers[0], numbers[-1])
    elif len(numbers) > 2:
        excluding_text = ' excluding {}, and {}'.format(', '.join(map(str, numbers[:-1])), numbers[-1])

    # Text to prmopt for
    prompt = 'select {} # ({} thru {}{}): '.format(index, min_val, max_val, excluding_text)

    # Prompt until number is accepted.
    while True:
        num = prompt_for_number(prompt, min_val, max_val)
        if num in numbers:
            print('{} has already been picked.'.format(num))
        else:
            break

    numbers.append(num)


def prompt_for_powerball():
    """
    Prompts user for their PowerBall number, enforcing ranges for PowerBall.
    :return:
    """
    minval = 1
    maxval = 26
    prompt = 'select Power Ball # ({} thru {}): '.format(minval, maxval)
    return prompt_for_number(prompt, minval, maxval)


def create_ticket(entries):
    """
    Creates a ticket from all entries based on the following rules:
        The numbers in the ticket must be randomly picked from the most common favorite numbers.
        The first five numbers cannot have repeats.
    :param entries: list of entries of favorite numbers
    :return: list of numbers
    """
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
    """
    Prompts user for a non-empty entry.
    :param prompt: what to display to request input
    :return:
    """
    while True:
        val = input(prompt).strip()
        if val:
            break
        print('Empty input is not allowed.')

    return val


def new_entry():
    """
    Prompts user for new employee entry of favorite numbers.
    :return: entry collected
    """
    first_name = non_empty_prompt('Please enter your first name: ')
    last_name = non_empty_prompt('Please enter your last name: ')
    name = '{} {}'.format(first_name, last_name)

    numbers = []
    favorite_count = 5
    for i in range(favorite_count):
        prompt_for_favorite(numbers)

    powerball = prompt_for_powerball()
    numbers.append(powerball)

    print('Entry added!')
    return Entry(name=name, numbers=numbers)


def print_results(powerball, entries):
    """
    Prints the results of the entries and ticket.
    :param powerball: list of winning numbers
    :param entries: list of employee entries
    :return: None
    """
    for entry in entries:
        print('{} {} PowerBall: {}'.format(entry.name, ' '.join(map(str, entry.numbers[0:5])), entry.numbers[5]))

    print()
    print('PowerBall winning number: ')
    print('{} PowerBall: {}'.format(' '.join(map(str, powerball[0:5])), powerball[5]))


def main_menu():
    """
    Interface of main application.
    :return: None
    """
    entries = []
    print('Welcome to the PowerBall ticket generator. Please select an option: ')
    while True:
        print('Main menu')
        print('a. Add new numbers for an employee.')
        if len(entries) > 1:
            print('g. Generate PowerBall ticket.')
            prompt = 'add, generate, or quit? [a, g, q]: '
        else:
            prompt = 'add or quit? [a, q]: '
        print('q. Quit this program.')

        choice = non_empty_prompt(prompt)

        if choice.lower() == 'a':
            entries.append(new_entry())
        elif choice.lower() == 'g':
            powerball = create_ticket(entries)
            print_results(powerball, entries)
        elif choice.lower() == 'q':
            print('Exiting.')
            break

        print()


if __name__ == '__main__':
    main_menu()
