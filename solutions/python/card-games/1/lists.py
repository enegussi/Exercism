"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    result = [number, ]
    for _ in range(2): 
        number += 1
        result.append(number)

    return result

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    return number in rounds

def card_average(hand):
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    actual_average = sum(hand) / len(hand)
    approx_average = (hand[0] + hand[-1]) / 2

    mid = len(hand)//2
    median = hand[mid]

    return approx_average == actual_average or median == actual_average

def average_even_is_average_odd(hand):
    evens = hand[0::2]
    odds = hand[1::2]
    
    if not evens or not odds:
        return False

    even_avg = sum(evens) / len(evens)
    odd_avg = sum(odds) / len(odds)

    return even_avg == odd_avg

def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = 22

    return hand
    
    
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    pass
