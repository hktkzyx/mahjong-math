import numpy as np
from scipy import special


def prob_get_expected_after_certain_turn(turns_later: int, turns_remain: int,
                                         tiles_expect: int) -> float:
    """The probability of get expected tile after `turns_later` set of turns.

    :param turns_later: Get the expected tile after `turns_after` set of turns
    :param turns_remain: The remaining turns
    :param tiles_expect: The number of expected tiles
    :return: Probability
    """
    tiles_remain = 4 * turns_remain + 14
    if tiles_expect > turns_later:
        greater = tiles_remain - turns_later
        less = tiles_remain - tiles_expect
    else:
        greater = tiles_remain - tiles_expect
        less = tiles_remain - turns_later
    numerator, denominator = 1, 1
    i, j = less, greater
    while i > tiles_remain - turns_later - tiles_expect:
        numerator = numerator * i
        i = i - 1
    while j > greater:
        denominator = denominator * j
        j = j - 1
    return numerator / denominator