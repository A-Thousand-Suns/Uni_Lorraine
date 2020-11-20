#!/usr/bin/env python
# coding: utf-8

# # Lab 2: Reviewing Syntax

# ## Goals
# Welcome to your second lab day! 
# The primary goal of this lab is to make sure that you master basic python syntax.
# 
# Most of what we'll see during this lab is things you're already somewhat familiar with. As a consequence, many of the exercises are about correcting faulty syntax. Tracking and correcting buggy code, be it syntactically wrong or semantically faulty, is a major part of day-to-day programming. Better get you used to it!
# **Tip:** _Don't hesitate to open up previous class materials and refer to it, as it might prove helpful._
# 
# As always, your exercises will be corrected and graded automatically. Make sure to convert your notebooks to .py scripts and submit those through Arche. Be careful about naming schemes: John DOE's submitted script should be named `tp2_john_doe.py`. **Remember to test your script after converting!** Running a simple `python3 tp2_john_doe.py` should be the _bare_ minimum. 

# ## Conditional execution
# 
# "Conditional execution" is just a fancy way of saying "run the instruction, if and only if a certain condition applies".
# 
# Typically, in python, we use the keyword `if`, followed by a condition (anything that can be evaluated as `True` or `False`) and a colon (`:`) for that purpose. Instructions that are to be conditionally executed are to be indented. For example:
# 
# ```
# if number_of_peanuts_i_have > 42:
#     give_peanuts_to_everyone()
# ```
# 
# In the case you want to define a behavior if the condition fails, use the `else` keyword:
# 
# ```
# if number_of_peanuts_i_have > 42:
#     give_peanuts_to_everyone()
# else:
#     eat_peanuts_in_secret()
# ```
# 
# If you want to define a behavior in case your first `if` condition fails, but depending on some second condition, use the `elif` (as in, "else if") keyword:
# 
# ```
# if number_of_peanuts_i_have > 42:
#     give_peanuts_to_everyone()
# elif number_of_peanuts_i_have > 10:
#     give_peanuts_to_close_friends_only()
# else:
#     eat_peanuts_in_secret()
# ```

# ### Exercise #1 : Fix it!
# 
# Below is a cell containing syntactically wrong conditional instructions. Fix them!
# 
# **Tip:** _Running a cell to test how it behaves and whether it is correct is a good practice. Pay attention to the error messages you get: they give valuable hint as to what you need to fix!_

# In[ ]:


some_value = 42
   
if some_value ==42:
    print("I am a DJ")
elif some_value >= 43:
    print("kangaroo")
else:
    if some_value <= 43:
        print("didgeridoo")
    else:
        print("berimbau")


# ## Any value can pass as a test
# 
# One important point in python is that virtually any value can be used as a condition. 
# 
# We divide values between *truthy* and *falsy* values. By default, all values are truthy: when put after an `if`, they will be evaluated as if they were `True`.
# 
# The exceptions to that are:
# 
#  - The `False` boolean value
#  - Boolean statement that evaluate to `False`: e.g., `42 < 2`
#  - Values equal to zero: for example `0`, `0.0`
#  - The empty string: `""`
#  - The special `None` object
# 
# All of these are falsy and will be evaluated as if they were `False` in conditional instructions.

# ### Exercise #2 : Which is syntactically wrong?
# 
# The consequence of all values being either `falsy` or `truhty` is that the syntax of conditions is very flexible! Below are a number of conditional instruction blocks. Remove only those blocks that are syntactically incorrect!

# In[ ]:


# Block 2
if print:
    print(print)


    
# Block 5
if "":
    print("Alack")
elif "Shakespeare":
    print("poor")
else:
    print("Yorrick")


# ## Being in the loop
# 
# Another very important aspect of python syntax is the  ability to loop over a series of instruction. Python offers two means of achieving this.
# 
# The first one is called a `while` loop, as it uses the `while` keyword. It basically repeats the same instructions over and over, stoping only when the condition after the `while` keyword is falsy:
# 
# ```
# while i_have_some_peanuts():
#     eat_one_peanut()
# ```
# 
# Badly written `while` loops can be dangerous: if the condition never gets falsy (e.g., if I have an infinite supply of peanuts! ... or if I forget to subtract eaten peanuts from the total number of remaining peanuts) then the code will **never** stop.
# 
# The second means of looping over instructions is called a `for` loop. It iterates over each element in a collection for instance, items in a list, or characters in a string), and stops when there are no more. Each element, in turn, is stored in the variable declared right after the `for` keyword. We put the collection after an `in` keyword. For example:
# 
# ```
# for my_peanut in all_the_peanuts_i_have():
#     eat(my_peanut)
# ```

# ### Exercise #3 : Somebody make it stop!
# 
# The following code cell contains a never-ending `while` loop. Spot the mistake and correct it, so that the execution stops after 42 loops.

# In[ ]:


i = 21
n = 42

# this loop will never stop, why?
while n > 0:
    i -= 1
    n -= 1


# ### Exercise #4 : 99 Bottles of beer on the wall
# 
# One (somewhat) famous song in code programming is called ["99 bottles of beer"](https://en.wikipedia.org/wiki/99_Bottles_of_Beer). It's frequently used to demonstrate the ability of a programming language to loop over a series of instructions. The song goes like this:
# 
# > 99 bottles of beer on the wall, 99 bottles of beer on the wall,
# 
# > Take one down, pass it around, 98 bottles of beer on the wall
# 
# > 98 bottles of beer on the wall, 98 bottles of beer on the wall,
# 
# > Take one down, pass it around, 97 bottles of beer on the wall
# 
# ... and so on, until there are no more bottles to pass around:
# 
# > 1 bottle of beer on the wall, 1 bottle of beer on the wall,
# 
# > Take one down, pass it around, no more bottle of beer on the wall
# 
# 
# In the next code cell, write a series of instruction that prints the entire song, from 99 down to 0. *Be careful about plurals and singulars! After all, English syntax deserves as much respect as python syntax.*
# 
# **Challenge:** &#9971; Golf it! If you don't know, in programming, golfing means "writing some piece of code with as few characters as possible". 

# In[ ]:


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


# ### Exercise #5 : All this while I didn't know
# 
# The next exercise is about writing a function to discover the value of a secret integer!
# 
# You might know this game as "hot or cold". We randomly select one integer between 1 and 100 (included). 
# 
# You have to implement the function `find_mystery_number()` such that when called, it returns the mystery number. Your function **must not** refer to the mystery number. Instead, you **must** use the function `hot_or_cold()` to see whether your current guess is correct or not.
# 
# **Challenge 1:** Try to make as few guesses as possible!
# 
# **Challenge 2:** &#9971; Golf it!

# In[ ]:


import random

# this is for replicability
random.seed(a=42)

# this is the secret number to guess. Don't look at it!
_THE_MYSTERY_NUMBER = random.randint(1, 100)


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


# ## Done Early?  Bonus Exercise
# 
# ### Exercise #6 : Collatz Sequence
# 
# You may have seen this problem before.
# 
# The *Collatz sequence* is an iterative sequence defined on the positive integers by:
# 
# ```
# n -> n / 2    if n is even
# n -> 3n + 1   if n is odd
# ```
# 
# For example, using the rule above and starting with 13 yields the sequence:
# 
# ```
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# ```
# 
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although unproven, it it hypothesized that all starting numbers finish at 1.
# 
# What is the length of the longest chain which has a starting number under 1000?
# 
# *NOTE: Once the chain starts the terms are allowed to go above one thousand.*
# 
# **Challenge 1**: Same question, but for any starting number under 1,000,000 (you may need to implement a cleverer-than-naive algorithm)
# 
# **Challenge 2**:  &#9971; Golf it! Keep your algorithm as efficient as possible, and your code as small as you can!

# In[ ]:


def collatz_len(n):
    """Computes the length of the Collatz sequence starting at `n`."""
    length = 1
    if n <= 1:
        return 1

    while n != 1:
        if(n % 2) == 0:
            n = n / 2
            length += 1

        elif(n % 2) == 1:
            length += 1
            n = 3*n+1
    
    return length

def max_collatz_len(n):
    """Computes the longest Collatz sequence length for starting numbers < `n`"""
    lenDict = 0  # num:len
    for i in range(1, n):
        len = collatz_len(i)
        if len > lenDict:
            lenDict = len

    return lenDict

print(max_collatz_len(1000))
print(max_collatz_len(1000000))


# ## Submitting Labs
# 
# Alright, you did it! Enough beers and peanuts for today.
# 
# Submit your work on Arche. And remember:
# 
#  1. **Convert it** to python script
#  1. **Test it** to verify it doesn't crash
#  1. **Name it** correctly so it can be automatically graded

# Credits go to CS41 authors (@sredmond) for the original Collatz problem.
# 
# > Adapted with <3 and peanuts by tmickus
