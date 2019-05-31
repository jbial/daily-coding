"""
This problem was asked by Facebook.

Given a function that generates perfectly random numbers
between 1 and k (inclusive), where k is an input,
write a function that shuffles a deck of cards represented
as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.

solution:
Iterate through the deck, each time using the RNG to generate a random position
between one and 52 - current_position - 1, then swap the current position with
the random shifted one.
"""
from random import randint

def get_randint(k):
    return randint(0, k)


def shuffle_deck(num_cards=52):
    """Shuffles a 52 card deck using only swaps
    """
    deck = [i for i in range(num_cards)]

    # get shifted positions and swap
    for old_index in deck:
        new_index = old_index + get_randint(num_cards - old_index - 1)
        temp = deck[new_index]
        deck[new_index] = deck[old_index]
        deck[old_index] = temp
    return deck


def main():
    
    if all(x in shuffle_deck() for x in range(52)):
        print([i for i in range(52)])
        print(shuffle_deck())
        print("Passed")
    else:
        print("Failed")


if __name__ == '__main__':
    main()

