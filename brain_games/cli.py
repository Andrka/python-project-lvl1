# -*- coding:utf-8 -*-

"""Command line interface."""

import prompt

from brain_games import games


def welcome_user() -> str:
    """Greet user and return taken name."""
    print()
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def take_str_answer() -> str:
    """Take string answer from user."""
    return prompt.string('Your answer: ')


def take_int_answer() -> int:
    """Take int answer from user."""
    return prompt.integer('Your answer: ')


def ask_question(phrase: str):
    """Ask user the question."""
    print('\nQuestion: {0}\n'.format(phrase))


FONT_RED = '\033[91m'
FONT_END = '\033[0m'


def paint_to_red(text: str) -> str:
    """Paint text to red."""
    return '{0}{1}{2}'.format(FONT_RED, text, FONT_END)


FONT_BLUE = '\033[96m'


def paint_to_blue(text: str) -> str:
    """Paint text to blue."""
    return '{0}{1}{2}'.format(FONT_BLUE, text, FONT_END)


FONT_BOLD = '\033[1m'


def paint_to_bold(text: str) -> str:
    """Paint text to bold."""
    return '{0}{1}{2}'.format(FONT_BOLD, text, FONT_END)


def print_when_lose_game(
    name: str,
    user_answer: str,
    correct_answer: str,
):
    """End game with wrong answer."""
    message = ''.join((
        paint_to_red("'{0}'").format(user_answer),
        ' is wrong answer ;',
        paint_to_bold('('),
        paint_to_blue('.'),
        ' Correct answer was ',
        paint_to_red("'{0}'").format(correct_answer),
        paint_to_blue('.\n'),
        'Let',
        paint_to_red("'s try again, {0}!").format(name),
    ))
    print(message)


def print_when_right_answer():
    """Notify user about right answer."""
    print('Correct!')


def print_when_win_game(name: str):
    """End game with right answers."""
    print('Congratulation, {0}!'.format(name))


def print_start_message():
    """Show start message."""
    print('\nWelcome to the Brain Games!')


def print_rules(rules: str):
    """Show game rules."""
    print('\n', rules, sep='')


GAMES = (
    ('calc game', games.calc),
    ('even game', games.even),
    ('gcd game', games.gcd),
    ('prime game', games.prime),
    ('progression game', games.progression),
)


def print_available_games():
    """Print available games to choose."""
    print('Choose game to play:')
    for index, game in enumerate(GAMES):
        print('{0} - {1}'.format(index + 1, game[0]))
    print()
