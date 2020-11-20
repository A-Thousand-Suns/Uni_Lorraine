
# coding: utf-8

# # Lab 1: Welcome to Python!

# ## Goals
# Welcome to your first lab day! These practical sessions are designed to be your opportunity to experiment with Python and gain hands-on experience with the language.
# 
# The primary goal of this lab is to ensure that your Python installation process went smoothly, and that there are no lingering Python 3 bugs floating around. Don't be shy, and make sure to speak out if you encounter an issues: tutors are here to help.
# 
# This lab also gives you the chance to write what might be your first programs in Python and allows you to experiment with both scripts and with the interactive interpreter!
# 
# These problems are not intended to be algorithmically challenging - just ways to flex your new Python 3 muscles. Even if the problems seem simple, work through them quickly, and then you're free to go. 
# 
# As always, have fun, and enjoy the (remainder of the) class period!

# ## Naming conventions
# 
# We've adapted the labs you'll be working on from Stanford's CS41 materials. One of the things we'll be doing differently is the grading process. For your practicals, we'll be relying on automatic grading. 
#  + On your side, the first thing you need to make sure of is that you've submitted your lab **as a python script**.
#  + To convert a Jupyter notebook into a script, use the command `jupyter nbconvert --to script {YOUR_NOTEBOOK}.ipynb`.
#  + You must ensure that your final python script is correctly named `tp{SESSION_NUMBER}_{YOUR_FIRSTNAME}_{YOUR_LASTNAME}.py`, in lowercase. For instance, Jane Doe's submission for this lab should be called `tp1_jane_doe.py`.
#  + Within the code, you will also need to follow namingrequirements **strictly**. If the instructions ask for a function with a specfic name, make sure your function has that exact name. If you are asked to declare a variable with a specific name, _again_: make sure to match the instructions **exactly**.
#  
# 

# ### A first exercise to make sure you get the point:
# 
# * Declare a variable called `something_very_important` that stores the value `42`

# In[ ]:

something_very_important = 42

# * Create a function called `my_add_function(a, b)`, that takes two integers and returns their sum:

# In[ ]:

def my_add_function(a:int, b:int):
    return a + b


# **NB:** You might have noticed that we name functions and variables with lowercased words separated by underscores (`_`). It's a naming convention widely shared across the Python community, and it's good practice for you to also follow this pattern!

# ## Common mistakes
# 
# Here are a list of mistakes we frequently encounter when reviewing your work.
# 
# 1. `print(result)` **instead of** `return result`. While these two might seem to produce the same thing, they are actually quite different. Whatever you pass to the `print()` function will be displayed on screen. When you use the `return` keyword, you stop the execution of a function and pass on its result to the script for further work.
# 1. **Type mismatches!** When you test a function you've implemented, make sure that the arguments are of the correct type. For instance, the string `"42"` is different from the integer `42`. Python has a function `type(x)` that will tell you the type of the argument `x`.
# 1. problems with Jupyter code **cells execution order**. While Jupyter is awesome when it comes to fiddling with script, often, you may be tempted to edit some code you've written in a previous cell, run this previous cell, and then go back to work wherever you were before that. As a result, other cells that depended on the previous implementation might cease to function properly! As a rule of thumb, you should make sure that cells are executed from top to bottom. **Tip:** the number in square brackets next to a code cell corresponds to the order in which you've ran the code cells.
# 1. **Not testing your code after you've tweaked it.** Many, many silly mistakes come from not running your code once after doing "just a simple modification". Always test!

# ### Another exercise to make sure you get the point
# 
# Have a look at the instructions in the following code cell, and try to predict what they will produce. You can run the code to check your answers using the `Run` button.

# In[ ]:

# SOLUTION: We expect the line below to print 42 and then return False: the return value of the print() function is always None.
print(something_very_important) == my_add_function(32, 10)
# SOLUTION: We expect the line below to return the string "3210": the plus operator for strings corresponds to concatenation
my_add_function("32", "10")


# ## Zen of Python
# 
# Run the following code cell by selecting the cell and pressing Shift+Enter.
# 

# In[ ]:


import this


# ## Hello World
# 
# Edit the following cell so that it prints `"Hello, world!"` when executed.

# In[ ]:

print("Hello, world!")


# ### Fizz, Buzz, FizzBuzz!
# If we list all of the natural numbers under 41 that are a multiple of 3 or 5, we get
# 
# ```
#  3,  5,  6,  9, 10, 12, 15,
# 18, 20, 21, 24, 25, 27, 30,
# 33, 35, 36, 39, 40
# ```
# 
# The sum of these numbers is 408.
# 
# Immplement a function called `fizzbuzz(n)` and use it to find the sum of all the multiples of 3 or 5 below 1001.

# In[ ]:


def fizzbuzz(n:int):
    """Returns the sum of all numbers < `n` divisible by 3 or 5."""
    total = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

fizzbuzz(1001)


# ### Fahrenheit-to-Celsius converter
# Write a program to convert degrees Fahrenheit to degrees Celcius which (1) takes as argument a number (not necessarily integral) representing the current temperature in degrees Fahrenheit, (2) converts that value into the equivalent degrees Celsius, and (3) **prints** the final equivalent value.
# 
# For example, your program should be able to emulate the following three sample runs:
# 
# ```
# Temperature F? 212
# It is 100.0 degrees Celsius.
# 
# Temperature F? 98.6
# It is 37.0 degrees Celsius.
# 
# Temperature F? 10
# It is -12.222222222222221 degrees Celsius.
# ```
# 
# Want to be fancy (challenge)? Try to print the final temperature to two decimal places. *Hint: Take a look at the [`round()`](https://docs.python.org/3.4/library/functions.html#round) function. Isn't Python great?*

# In[ ]:


def convert_fahr_to_cels(deg_fahr:float):
    print(round((deg_fahr - 32) * 5 / 9, 2))


# ## Bonus Challenges
# 
# Don't worry about getting to these bonus problems. In most cases, bonus questions ask you to think more critically or use more advanced algorithms. 

# ### Zen Printing
# 
# Write a series of instructions using `print()` that, when run, prints out a tic-tac-toe board.
# 
# ````
#  X | . | . 
# -----------
#  . | O | . 
# -----------
#  . | O | X 
# ````
# 
# You may find the optional arguments to `print()` useful, which you can read about [here](https://docs.python.org/3/library/functions.html#print). In no more than five minutes, try to use these optional arguments to print out this particular tic-tac-toe board.

# In[ ]:

print(" X", ".", ".", sep=" | ", end=" \n-----------\n")
print(" .", "O", ".", sep=" | ", end=" \n-----------\n")
print(" .", "O", "X", sep=" | ", end=" \n")

# Print a tic-tac-toe board using optional arguments.


# Maybe you were able to print out the tic-tac-toe board. Maybe not. In the five minutes you've been working on that, I've gotten bored with normal tic-tac-toe (too many ties!) so now, I want to play SUPER tic-tac-toe.
# 
# Write a program that prints out a SUPER tic-tac-toe board.
# 
# ```
#   |  |  H  |  |  H  |  |  
# --+--+--H--+--+--H--+--+--
#   |  |  H  |  |  H  |  |  
# --+--+--H--+--+--H--+--+--
#   |  |  H  |  |  H  |  |  
# ========+========+========
#   |  |  H  |  |  H  |  |  
# --+--+--H--+--+--H--+--+--
#   |  |  H  |  |  H  |  |  
# --+--+--H--+--+--H--+--+--
#   |  |  H  |  |  H  |  |  
# ========+========+========
#   |  |  H  |  |  H  |  |  
# --+--+--H--+--+--H--+--+--
#   |  |  H  |  |  H  |  |  
# --+--+--H--+--+--H--+--+--
#   |  |  H  |  |  H  |  |  
# ```
# 
# You'll find that there might be many ways to solve this problem. Which do you think is the most 'pythonic?' Talk to someone next to you about your approach to this problem. Remember the Zen of Python!

# In[ ]:

# SOLUTION: How to approach this problem? 
# we can see there are three repeating sets of lines. One of the main mantras of Python devs is DRY: Don't Repeat Yourself.

_three_cells = "  |  | "
_three_floors = "--+--+--"
_big_block_floor = "=" * 8

def _print_thrice(pattern, sep="H"):
    print(*[pattern] * 3, sep=sep)

for _big_block_number in range(1, 4):
    for _small_block_number in range(1, 4):
        _print_thrice(_three_cells)
        if _small_block_number < 3:
            _print_thrice(_three_floors)
    if _big_block_number < 3:
        _print_thrice(_big_block_floor)


# ## Done Early?
# 
# Read [Python’s Style Guide](https://www.python.org/dev/peps/pep-0008/), keeping the Zen of Python in mind. In what ways do you notice that Python's style guidelines are influence by Python's core philosophy? Some portions of the style guide cover language features that we haven't yet touched on in class - feel free to skip over those sections for now.

# ## Printing with format
# 
# There are three ways of formatting strings in Python

# In[4]:


name = 'James'
'Hello %s' %name


# In[ ]:


'My name is {1}, {0} {1}'.format('James', 'Bond')


# In[9]:


age = 21
print('I am {age} year old')
print(f'I am {age} year old')


# you can also control the printing, for example if you want to print the value of Pi with two digits.
# 
# First, import math. You can access to the value with 
# 
# '>>> math.pi'
# 

# In[ ]:

import math
print('pi: %f \nshort pi %0.2f' % (math.pi, math.pi))


# Please, refer to the mini language guide line
# https://docs.python.org/3/library/string.html#formatspec

# Write a program to print the square root of the parameter of the function such that it prints the parameter with 2 digits and the square root with 3.

# In[10]:

def sq_root(n:float):
    print("The square root of %.2f is %.3f" % (n, math.sqrt(n)))


# such that
# 
# sq_root(26)
# 
# The square root of 26.00 is 5.099
# 

# ## Submitting Labs
# 
# Alright, you did it! Make sure to convert your lab to a python script (cf. above), and then submit it through Arche.

# *Adapted in part from Stanford CS41 course.*
# 
# *Credit to ProjectEuler and InterviewCake for some problem ideas.*
# 
# > With <3 by @sredmond
