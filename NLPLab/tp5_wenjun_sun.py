#!/usr/bin/env python
# coding: utf-8

# # Lab 5: Functions

# ## Overview
# This lab is aimed at building familiarity with reading and writing Python functions with different types of formal parameters and explore some nuances of function execution semantics.
# 
# *Disclaimer: we know that this lab is particularly focused on Python semantics, which may not seem exciting at first. However, mastering the mechanics of Python functions gives you access to a whole lot of powerful tools that either don't exist or are uncommon or hard-to-use in other languages! The skills you learn through this lab will allow you to write (and debug) powerful Pythonic code quickly and easily!*
# 

# ## Review
# 
# As always, take a moment to read through the slides from this week at the [course website](https://stanfordpython.com/#lecture). In particular, pay attention to the quick overview of best practices in Python style mechanics.

# ## Exploring Arguments and Parameters
# 
# You can work through the following problems with a partner.

# 
# Consider the following function definition:
# 
# ```Python
# def print_two(a, b):
#     print("Arguments: {0} and {1}".format(a, b))
# ```
# 
# For each of the function calls, in the following cell, predict whether the call is valid or not. If it is valid, what will the output be? If it is invalid, what is the cause of the error?
# 
# ### Exercise #1 : Uncomment invalid function calls 

# In[94]:


# Before running me, predict which of these calls will be invalid and which will be valid!
# For valid calls, what is the output?
# For invalid calls, why is it invalid?
def print_two(a, b):
    print("Arguments: {0} and {1}".format(a, b))

# Uncomment one by one, and check you are correct,
# then comment back the calls that are invalid.
# print_two()
print_two(4, 1)
# print_two(41)
# print_two(a=4, 1)
# print_two(4, a=1)
# print_two(4, 1, 1)
# print_two(b=4, 1)
print_two(a=4, b=1)
print_two(b=1, a=4)
# print_two(1, a=1)
# print_two(4, 1, b=1)


# ### Default Arguments
# 
# Consider the following function definition:
# 
# ```Python
# def keyword_args(a, b=1, c='X', d=None):
#     print("a:", a)
#     print("b:", b)
#     print("c:", c)
#     print("d:", d)
# ```
# 
# ### Exercise #2 : Uncomment invalid function calls
# 
# For each of the function calls, in the following cell, predict whether the call is valid or not. If it is valid, what will the output be? If it is invalid, what is the cause of the error?

# In[95]:


# Before running me, predict which of these calls will be invalid and which will be valid.
# For valid calls, what is the output?
# For invalid calls, why is it invalid?
def keyword_args(a, b=1, c='X', d=None):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)
    
# Uncomment one by one, and check you are correct,
# then comment back the calls that are invalid.
keyword_args(5)
keyword_args(a=5)
keyword_args(5, 8)
keyword_args(5, 2, c=4)
keyword_args(5, 0, 1)
keyword_args(5, 2, d=8, c=4)
# keyword_args(5, 2, 0, 1, "")
# keyword_args(c=7, 1)
keyword_args(c=7, a=1)
keyword_args(5, 2, [], 5)
# keyword_args(1, 7, e=6)
keyword_args(1, c=7)
# keyword_args(5, 2, b=4)


# ### Exploring Variadic Argument lists
# As before, consider the following function definition: 
# 
# ```Python
# def variadic(*args, **kwargs):
#     print("Positional:", args)
#     print("Keyword:", kwargs)
# ```
# 
# For each of the function calls, in the following cell, predict whether the call is valid or not. If it is valid, what will the output be? If it is invalid, what is the cause of the error?
# 
# ### Exercise #3 : Uncomment invalid function calls

# In[107]:


# Before running me, predict which of these calls will be invalid and which will be valid!
# For valid calls, what is the output?
# For invalid calls, why is it invalid?
def variadic(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

# Uncomment one by one, and check you are correct,
# then comment back the calls that are invalid.
variadic(2, 3, 5, 7)
variadic(1, 1, n=1)
#variadic(n=1, 2, 3)
variadic()
variadic(cs="Computer Science", pd="Product Design")
# variadic(cs="Computer Science", cs="CompSci", cs="CS")
variadic(5, 8, k=1, swap=2)
variadic(8, *[3, 4, 5], k=1, **{'a':5, 'b':'x'})
variadic(*[8, 3], *[4, 5], k=1, **{'a':5, 'b':'x'})
variadic(*[3, 4, 5], 8, *(4, 1), k=1, **{'a':5, 'b':'x'})
variadic({'a':5, 'b':'x'}, *{'a':5, 'b':'x'}, **{'a':5, 'b':'x'})


# ### Putting it all together
# 
# Often, however, we don't just see keyword arguments of variadic parameter lists in isolated situations. The following function definition, which incorporates positional parameters, keyword parameters, variadic positional parameters, keyword-only default parameters and variadic keyword parameters, is valid Python code. 
# 
# ```Python
# def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options):
#     print("x:", x)
#     print("y:", y)
#     print("z:", z)
#     print("nums:", nums)
#     print("indent:", indent)
#     print("spaces:", spaces)
#     print("options:", options)
# ```
# 
# For each of the function calls, in the following cell, predict whether the call is valid or not. If it is valid, what will the output be? If it is invalid, what is the cause of the error?
# 
# ### Exercise #4 : Uncomment invalid function calls

# In[119]:


# Before running me, predict which of these calls will be invalid and which will be valid!
# For valid calls, what is the output?
# For invalid calls, why is it invalid?
def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options):
    print("x:", x)
    print("y:", y)
    print("z:", z)
    print("nums:", nums)
    print("indent:", indent)
    print("spaces:", spaces)
    print("options:", options)
    
# Uncomment one by one, and check you are correct,
# then comment back the calls that are invalid.
# all_together(2)
all_together(2, 5, 7, 8, indent=False)
all_together(2, 5, 7, 6, indent=None)
# all_together()
# all_together(indent=True, 3, 4, 5)
# all_together(**{'indent': False}, scope='maximum')
all_together(dict(x=0, y=1), *range(10))
# all_together(**dict(x=0, y=1), *range(10))
# all_together(*range(10), **dict(x=0, y=1))
all_together([1, 2], {3:4})
# all_together(8, 9, 10, *[2, 4, 6], x=7, spaces=0, **{'a':5, 'b':'x'})
all_together(8, 9, 10, *[2, 4, 6], spaces=0, **{'a':[4,5], 'b':'x'})
all_together(8, 9, *[2, 4, 6], *dict(z=1), spaces=0, **{'a':[4,5], 'b':'x'})


# ## Writing Functions

# ### Exercise #5 : `speak_excitedly`
# Write a function `speak_excitedly` that accepts one required positional argument (a message) and two optional keyword arguments `n_excl_marks` and `in_caps`, the first of which is a positive integer referring to the number of exclamation marks to put at the end of the message (defaulting to `1`), and the second of which is a boolean flag indicating whether or not to capitalize the message (defaulting to `False`).
# 
# What would the function signature and implementation look like for this function?

# In[120]:


def speak_excitedly(message, n_excl_marks=1, in_caps=False):
    """Print a message, with an optional number of exclamation points and optional capitalization."""
    result = message[:] + "!"* n_excl_marks
    if in_caps:
        result = result.upper()
    return result


# How would you call this function to produce the following outputs?
# 
# ```Python
# "I love Python!!"
# "Keyword arguments are great!"
# "I guess Java is okay..."
# "LET'S GO CHIMPS!!!!!"
# ```

# In[121]:


speak_excitedly("I love Python", 2)  # => "I love Python!!"
speak_excitedly("Keyword arguments are great")  # => "Keyword arguments are great!"
speak_excitedly("I guess Java is okay...", 0)  # => "I guess Java is okay..."
speak_excitedly("Let's go chimps", 5, True)  # => "LET'S GO CHIMPS!!!!!"


# ### Exercise #6 : `average`
# Write a function `average` that accepts a variable number of integer positional arguments and computes the average. If no arguments are supplied, the function should return `None`.
# 
# What would the function signature and implementation look like for this function?

# In[122]:


def average(*args):
    """Return the average of numeric arguments or None if no arguments are supplied."""
    sum = 0
    if len(args) == 0:
        return None
    for num in args:
        sum += num
    return sum / len(args)


# It should be possible to call the function as follows:
# 
# ```Python
# average()  # => None
# average(5)  # => 5.0
# average(6, 8, 9, 11)  # => 8.5
# ```

# In[123]:


print(average())  # => None
print(average(5))  # => 5.0
print(average(6, 8, 9, 11))  # => 8.5


# Suppose that we have a list `l = [???]` supplied by the user (or some file!) of unknown contents. How can we use the `average` function we just wrote to compute the average of this list? For this part of the problem, do not use the builtin `sum` or `len` functions – try unpacking the contents of `l` into `average`.

# In[125]:


l = [3, 1, 41, 592, 65358]

print(average(*l))


# ### Exercise #7 : `make_table` (bonus challenge)
# 
# Write a function to make a table out of an arbitrary number of keyword arguments. For example, 
# 
# ```Python
# make_table(
#     first_name="Sam",
#     last_name="Redmond",
#     shirt_color="pink"
# )
# ```
# 
# should produce
# 
# ```
# =========================
# | first_name  |     Sam |
# | last_name   | Redmond |
# | shirt_color |    pink |
# =========================
# ```
# 
# Additionally, there should be two parameters, `key_justify` and `value_justify`, whose default values are `'left'` and `'right'` respectively. These keyword arguments will control the text alignment for keys and values in the table. Valid options for these parameters are `['left', 'right', 'center']`. There should be an extra space of padding on either side of the keys and values. As another example,
# 
# ```Python
# make_table(
#     key_justify="right",
#     value_justify="center",
#     song="Style",
#     artist_fullname="Taylor $wift",
#     album="1989"
# )
# ```
# 
# should produce
# 
# ```
# ==================================
# |            song |     Style    |
# | artist_fullname | Taylor $wift |
# |           album |     1989     |
# ==================================
# ```
# 
# What would the function signature and implementation look like for this function? Implement your code in the following cell.
# 
# Hint: you may find Python's string `.format()` [alignment specifiers](https://pyformat.info/#string_pad_align) useful.

# In[126]:


def make_table(key_justify='left', value_justify='right', **args):
    key_len = 0
    value_len = 0
    for key in args.keys():
        if key_len < len(key):
            key_len = len(key)
            
    for value in args.values():
        if value_len < len(value):
            value_len = len(value)

    justify = {'left':' <', 'right':' >', 'center':' ^'}
            
    print("=" * (7 + key_len + value_len))
    
    for i, j in args.items():
        print("| " + format(i, justify[key_justify]+str(key_len))+" | " + format(j, justify[value_justify]+str(value_len)) + " |")
        
    print("=" * (7 + key_len + value_len))
    


# ## Function Nuances

# ### Review #1: Return
# 
# Predict the output of the following code snippet.
# 
# ```Python
# def say_hello():
#     print("Hello!")
# 
# print(say_hello())  # => ?
# 
# def echo(arg=None):
#     print("arg:", arg)
#     return arg
# 
# print(echo())  # => ?
# print(echo(5)) # => ?
# print(echo("Hello")) # => ?
# 
# def drive(has_car):
#     if not has_car:
#         # Please never actually signal an error like this...
#         return "Oh no!"
#     return 100  # miles
# 
# print(drive(False))  # => ?
# print(drive(True))   # => ?
# ```
# 
# You can run the code in the following cell to check your hypothesis. If you made any incorrect predictions, talk to a partner about why!

# In[127]:


def say_hello():
    print("Hello!")

print(say_hello())  # => ?

def echo(arg=None):
    print("arg:", arg)
    return arg

print(echo())  # => ?
print(echo(5)) # => ?
print(echo("Hello")) # => ?

def drive(has_car):
    if not has_car:
        # Please never actually signal an error like this...
        return "Oh no!"
    return 100  # miles

print(drive(False))  # => ?
print(drive(True))   # => ?


# ### Review #2 : Parameters and Object Reference
# 
# *Optional Reading: [Jeff Knupp's Blog](https://jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither/)*
# 
# Suppose we have the following two functions:
# 
# ```Python
# def reassign(arr):
#     arr = [4, 1]
#     print("Inside reassign: arr = {}".format(arr))
# 
# def append_one(arr):
#     arr.append(1) 
#     print("Inside append_one: arr = {}".format(arr))
# ```
# 
# Predict what the following code snippet will output. What's the difference between the sections? What is the cause of this difference?
# 
# ```Python
# l = [4]
# print("Before reassign: arr={}".format(l))  # => ?
# reassign(l)
# print("After reassign: arr={}".format(l))  # => ?
# 
# l = [4]
# print("Before append_one: arr={}".format(l))  # => ?
# append_one(l)
# print("After append_one: arr={}".format(l))  # => ?
# ```
# 
# You can run the code in the following cell to check your hypothesis. 

# In[128]:


def reassign(arr):
    arr = [4, 1]
    print("Inside reassign: arr = {}".format(arr))

def append_one(arr):
    arr.append(1) 
    print("Inside append_one: arr = {}".format(arr))
    
l = [4]
print("Before reassign: arr={}".format(l))  # => ?
reassign(l)
print("After reassign: arr={}".format(l))  # => ?

l = [4]
print("Before append_one: arr={}".format(l))  # => ?
append_one(l)
print("After append_one: arr={}".format(l))  # => ?


# ### Review #3 : Scope
# *Optional Reading: [Python's Execution Model](https://docs.python.org/3/reference/executionmodel.html), especially Section 4.2.2.*
# 
# Try to predict the output of the following Python programs.
# 
# ```Python
# # Python program: Case 1
# x = 10
# 
# def foo():
#     print("(inside foo) x:", x)
#     y = 5
#     print('value:', x * y)
# 
# print("(outside foo) x:", x)
# foo()
# print("(after foo) x:", x)
# ```
# 
# 
# ```Python
# # Python program: Case 2
# x = 10
# 
# def foo():
#     x = 8  # Only added this line - everything else is the same
#     print("(inside foo) x:", x)
#     y = 5
#     print('value:', x * y)
# 
# print("(outside foo) x:", x)
# foo()
# print("(after foo) x:", x)
# ```
# 
# You can run the following cell to confirm or refute your hypothesis.
# 
# Try to draw a picture of the variable bindings at each scope (global scope and `foo` function-level scope) in each case. 

# In[129]:


# Case 1
x = 10

def foo():
    print("(inside foo) x:", x)
    y = 5
    print('value:', x * y)

print("(outside foo) x:", x)
foo()
print("(after foo) x:", x)


# In[130]:


# Case 2
x = 10

def foo():
    x = 8  # Only added this line - everything else is the same
    print("(inside foo) x:", x)
    y = 5
    print('value:', x * y)

print("(outside foo) x:", x)
foo()
print("(after foo) x:", x)


# ### Review #4 : UnboundLocalError
# 
# If we swap just two lines of code, something unusual happens. What is the error? Why might it be happening?
# 
# ```Python
# x = 10
# 
# def foo():
#     print("(inside foo) x:", x)  # We swapped this line
#     x = 8                        # with this one
#     y = 5
#     print('value:', x * y)
# 
# print("(outside foo) x:", x)
# foo()
# print("(after foo) x:", x)
# ```

# Similarly, `foo` as defined in
# 
# ```
# lst = [1,2,3]
# def foo():
#     lst.append(4)
# foo()
# ```
# 
# will compile (that is, the function object will be byte-compiled without problem), but
# 
# ```
# lst = [1,2,3]
# def foo():
#     lst = lst + [4]
# foo()
# ```
# 
# will raise an `UnboundLocalError`. 
# 
# 
# Why? It doesn't, surprisingly, have to do with the fact that `.append` is in place and `+` is not.
# 
# Use the following cells to make trials and understand.

# In[131]:


# This works
lst = [1,2,3]
def foo():
    lst.append(4)
foo()


# In[132]:


# This doesn't
lst = [1,2,3]
def _foo():
    lst = lst + [4]
# try it! uncomment the line to test it, and comment it back afterwards
#_foo()


# This is such a common problem that the Python FAQ has [a section](https://docs.python.org/3/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value) dedicated to this type of `UnboundLocalError`.
# 
# *Note, the `global` and `nonlocal` keywords can be used to assign to a variable outside of the currently active (innermost function) scope. If you're interested, you can read more about scoping rules in the optional reading, or in the [appropriate FAQ section](https://docs.python.org/3/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python).*

# ### Review #5 : Default Mutable Arguments - A Dangerous Game
# 
# A function's default values are evaluated at the point of function definition in the defining scope. For example:

# In[133]:


x = 5

def square(num=x):
    return num * num

x = 6
print(square())   # => 25, not 36
print(square(x))  # => 36


# **Warning: A function's default values are evaluated *only once*, when the function definition is encountered. This is important when the default value is a mutable object such as a list or dictionary**
# 
# Predict what the following code will do, then run it to test your hypothesis:
# 
# ```Python
# def append_twice(a, lst=[]):
#     lst.append(a)
#     lst.append(a)
#     return lst
#    
# # Works well when the keyword is provided
# print(append_twice(1, lst=[4]))  # => [4, 1, 1]
# print(append_twice(11, lst=[2, 3, 5, 7]))  # => [2, 3, 5, 7, 11, 11]
# 
# # But what happens here?
# print(append_twice(1))
# print(append_twice(2))
# print(append_twice(3))
# ```

# In[134]:


# Something fishy is going on here. Can you deduce what is happening?
def append_twice(a, lst=[]):
    lst.append(a)
    lst.append(a)
    return lst
   
# Works well when the keyword is provided
print(append_twice(1, lst=[4]))  # => [4, 1, 1]
print(append_twice(11, lst=[2, 3, 5, 7]))  # => [2, 3, 5, 7, 11, 11]

# But what happens here?
print(append_twice(1))
print(append_twice(2))
print(append_twice(3))


# After you run the code, you should see the following printed to the screen:
# 
# ```
# [1, 1]
# [1, 1, 2, 2]
# [1, 1, 2, 2, 3, 3]
# ```
# Discuss with a partner why this is happening.
# 
# If you don’t want the default value to be shared between subsequent calls, you can use a sentinel value as the default value (to signal that no keyword argument was explicitly provided by the caller). If so, your function may look something like:
# 
# ```Python
# def append_twice(a, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(a)
#     lst.append(a)
#     return lst
# ```
# 
# Discuss with a partner whether you think this solution feels better or worse.

# In[135]:


def append_twice(a, lst=None):
    if lst is None:
        lst = []
    lst.append(a)
    lst.append(a)
    return lst


# Sometimes, however, this odd keyword value initialization behavior can be desirable. For example, it can be used as a cache that is modifiable and accessible by all invocations of a function:
# 
# ```Python
# def fib(n, cache={0: 1, 1: 1}):
#    if n in cache:  # Note: default value captures our base cases
#        return cache[n]
#    out = fib(n-1) + fib(n-2)
#    cache[n] = out
#    return out
# ```
# 
# Try running the following code cells.

# In[136]:


def fib(n, cache={0: 1, 1: 1}):
   if n in cache:  # Note: starting values in the dictionary captures our base cases.
       return cache[n]
   out = fib(n-1) + fib(n-2)
   cache[n] = out
   return out

print(fib(10))  # => 89
print(fib.__defaults__[0])  # Access the cached dictionary.


# Cool, right? The cache follows the function around, as an attribute on the function object, rather than being the responsibility of the caller! Even so, there are better, more Pythonic ways to capture this particular cache design pattern (see [functools.lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache)). Nevertheless, it's a neat trick that might come in useful!

# ### Review #6 : Documentation (`__doc__`)
# 
# The first string literal in any function, if it comes before any expression, is bound to the function's `__doc__` attribute. 

# In[137]:


def my_function():
    """Summary line: do nothing, but document it.
        
    Description: No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)
# Summary line: Do nothing, but document it.
#
#     Description: No, really, it doesn't do anything.


# Lots of tools use these documentation strings to great advantage. For example, the builtin `help` function displays information from docstrings, and many API-documentation-generation tools like [Sphynx](http://www.sphinx-doc.org/en/stable/) or [Epydoc](http://epydoc.sourceforge.net/) use information contained in the docstring to form smart references and hyperlinks on documentation websites.
# 
# Furthermore, the [doctest](https://docs.python.org/3/library/doctest.html) standard library module, in it's own words, "searches [the documentation string] for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown." Cool!

# ### Review #7 : Parameter Annotations (`__annotations__`)
# 
# Python allows us to add type annotations on functions arguments and return values. This leads to a world of complex possibilities and is still fairly controversial in the Python ecosystem. Nevertheless, it can be used to communicate to your clients expectations for the types of arguments.
# 
# Importantly, Python doesn't actually do anything with these annotations and will not check that supplied arguments conform to the type hint specified. This language feature is only made available through the collection of function annotations.

# In[138]:


def annotated(a: int, b: str) -> list:
    return [a, b]

print(annotated.__annotations__)
# => {'b': <class 'str'>, 'a': <class 'int'>, 'return': <class 'list'>}


# But it's not because Python itself doesn't do anything with it that they are useless. For instance, we can leverage this to create random calls with arguments of valid types. That's what the automatic grading script uses.
# Other cool use cases include building some really neat runtime type-checkers for Python! 
# 
# #### "Ask forgiveness, not permission"
# 
# One important point in python programming philosophy is that you should trust programmers that will use your code. They are the ones responsible for using it wisely. You shouldn't coerce them into using it exactly as you've intended: they might have very good reasons for doing what they're doing (and if they break it, it's on *them*).
# 
# Which is why, in the case of arguments type, rather than something like that:
# 
# ```Python
# # case 1
# def my_add(a, b):
#     if type(a) != int or type(b) != int:
#         raise TypeError("not an int")
#     return a + b
# ```
# 
# ... or something like that:
# ```Python
# # case 2
# def my_add(a, b):
#     assert type(a) == type(b) == int, "not an int"
#     return a + b
# ```
# 
# you should just *document* the intended usage with type hinting:
# ```Python
# # case 3
# def my_add(a: int, b: int) -> int:
#     """
#     Addition of two integers `a` and `b`
#     """
#     return a + b
# ```
# 
# and trust the user to use it wisely. Errors (be it a `TypeError` as in case 1, or an `AssertionError` as in case 2) should be the consequence of *badly broken behavior*, not a means of control over how your code is used.
# 
# There are cases where using an `assert` statement, such as in case 2, may be useful: for instance when you're unsure of the exact behavior of your code, or when illegal types might produce desastrous consequences down the line. In short, these kinds of check should be reserved to prevent convoluted situations where you'd say "How did **that** get in *here*?" from happening. Do note that you can strip `assert` statements from python scripts by running them as `python -O my_script.py`.
# 
# For more info, check out [PEP 3107](https://www.python.org/dev/peps/pep-3107/) on function annotations or [PEP 484](https://www.python.org/dev/peps/pep-0484/) on type hinting (which was introduced in Python 3.5)

# ### Exercise #8 : Autodoc (bonus exercise)
# 
# Write a function `autodoc(f)` that takes a function `f` as argument, and appends a summary of the arguments and return type to the doc string.
# 
# For instance, given this function:
# ```Python
# def eat_one_peanut_each(chimps:str, number_of_peanuts:int) -> int:
#     """A daily occurrence."""
#     return number_of_peanuts - len(chimps.split())
# ```
# 
# The doc after your function should look like this:
# 
# ```
# A daily occurrence.
# ....chimps: `str`
# ....number_of_peanuts: `int`
# ....return: `int`
# ```

# In[139]:


def eat_one_peanut_each(chimps:str, number_of_peanuts:int) -> int:
    """A daily occurrence."""
    return number_of_peanuts - len(chimps.split())

def autodoc(f):
    # your code here

    print(f.__doc__)
    
    for key, value in f.__annotations__.items():
        print('....' + key + ': ' + '\'' + value.__name__ + '\'')

autodoc(eat_one_peanut_each)


# ## Finished Early?
# Scan through [PEP 8](https://www.python.org/dev/peps/pep-0008/), Python's official style guide, as well as [PEP 257](https://www.python.org/dev/peps/pep-0257/), Python's suggestions for docstring conventions, if you didn't get a chance to read them last week.

# ## Submitting Labs
# 
# You know the drill, mandrill!
# 
# Don't forget to submit your lab through Arche once you're done. And remember:
# 
#  1. **Convert it** to python script
#  
#      You can do so by typing `jupyter nbconvert --to script {YOUR_NOTEBOOK}.ipynb` into the command line.
#      
#      Alternatively, you can use Jupyter's interface to create your file.
#      
#      - On Jupyter Notebook, go to *File -> Download As -> Python (.py)*
#      
#      - On Jupyter Lab, go to *File -> Export Notebook As... -> Export Notebook to Executable Script*
#  1. **Test it** to verify it doesn't crash
#  1. **Name it** correctly so it can be automatically graded (Jane Doe's submission for this lab should be called `tp5_jane_doe.py`)
# 
# 
# *This lab is very much based on CS41's* 
# 
# **Major credit to PSF for incredibly clear/readable documentation making this all possible, as well as the linked resources.**

# > With <3 by @sredmond

# In[ ]:




