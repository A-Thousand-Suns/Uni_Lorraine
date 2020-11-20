from scipy.stats import binom, uniform
#E11
pass

#E12b
p = 0.2
n = 100
binom.cdf(40, 100, 0.2)
#E12c
mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')
#2
for i in range(3):
    print(i)

i = 21
n = 42

# this loop will never stop, why?
while n > 0:
    i -= 1
    n -= 1
    print(n)

# And now for 99 bottle of beers...
str1 = ' bottles of beer on the wall, '
str2 = ' bottles of beer on the wall,\n'
str3 = 'Take one down, pass it around, '
str4 = ' bottles of beer on the wall'
strFin = 'Take one down, pass it around, no more bottle of beer on the wall'

for i in range(99, 0, -1):
    if i != 1:
        print(str(i) + str1 + str(i) + str2 + str3 + str(i-1) + str4)
    else:
        print(str(i) + str1 + str(i) + str2 + strFin)

import random

# this is for replicability
random.seed(a=42)

# this is the secret number to guess. Don't look at it!
_THE_MYSTERY_NUMBER = random.randint(1, 100)
print(_THE_MYSTERY_NUMBER)


def hot_or_cold(guess_number):
    """
    Oracle function to tell how far your guess is from the truth.
    """
    if guess_number == _THE_MYSTERY_NUMBER:
        return "bingo bango!"
    elif _THE_MYSTERY_NUMBER - 5 < guess_number < _THE_MYSTERY_NUMBER + 5:
        return "you're hot!"
    elif _THE_MYSTERY_NUMBER - 10 < guess_number < _THE_MYSTERY_NUMBER + 10:
        return "you're warm!"
    elif _THE_MYSTERY_NUMBER - 20 < guess_number < _THE_MYSTERY_NUMBER + 20:
        return "uh... not really..."
    else:
        return "cold. so cold."


def find_mystery_number():
    # your code goes here!
    while True:
        guess = float(input())
        result = hot_or_cold(guess)
        if result == "bingo bango!":
            print(result)
            break
        else:
            print(result)


def collatz_len(n):
    """Computes the length of the Collatz sequence starting at `n`."""
    length = 1
    if n <= 1:
        return 1

    while n != 1:
        if (n % 2) == 0:
            n = n / 2
            length += 1

        elif (n % 2) == 1:
            length += 1
            n = 3 * n + 1

    return length


def max_collatz_len(n):
    """Computes the longest Collatz sequence length for starting numbers < `n`"""
    lenDict = 0  # num:len
    for i in range(1, n):
        len = collatz_len(i)
        if len > lenDict:
            lenDict = len

    return lenDict


print(max_collatz_len(100000))
#print(max_collatz_len(1000000))