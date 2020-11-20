#!/usr/bin/env python
# coding: utf-8

# # Lab 4: Lists, tuples and dicts

# ## Overview
# 
# Welcome to your fourth lab! 
# 
# The primary goal of this lab is to focus on using data structures to solve some interesting problems. If you're curious and want to get to the bottom of what we're presenting here, go [check out Sequence types and Mapping types](https://docs.python.org/3/library/stdtypes.html)!
# 
# You're welcome to work in groups or individually. Remember to have some fun! Make friends and maybe relax a little too. 
# 
# **Note: These labs are *designed* to be long! Work through as much as you can in the time allotted, but also feel free to skip from question to question freely. The extra problems are intended to be extra practice, if you want to hone your Python skills even more.**
# 
# 
# As always, remember to submit your notebook as a script once you're done!
# 
# If you're done early: &#9971; Golf your functions! Make sure not to change the function names, so as to not mess up with the automatic grading down the line.
# 
# Above all, have fun playing with Python! Enjoy. 

# ## Lists
# 
# 
# Lists are one of python's most basic data structures. They correspond to mutable ordered sequences. 
# 
# - As sequences, they contain a series of elements.
# - As they are ordered, elements are guaranteed to come up in a certain order when you iterate over the list
# - As they are mutable, you can add and remove things from a list without having to create a new one.

# ### What's in it for you?
# 
# Predict what the following lines of Python will do. Then, run the code block below to see if they match what you expect:
# 
# ```Python
# s = [0] * 3
# print(s)
# s[0] += 1
# print(s)
# 
# s = [''] * 3
# print(s)
# s[0] += 'a'
# print(s)
# 
# s = [[]] * 3
# print(s)
# s[0] += [1]
# print(s)
# ```

# In[1]:


# Explore the elements of lists. Is the output what you expect?
s = [0] * 3
print(s)
s[0] += 1
print(s)

s = [''] * 3
print(s)
s[0] += 'a'
print(s)

s = [[]] * 3
print(s)
s[0] += [1]
print(s)


# Why is this happening? Consider using the `id` function to investigate further. What happens when we replace the second-to-last line with `s[0] = s[0] + [1]`? What if we replace the line with `s[0].append(1)`?

# ### Manipulating lists
# 
# Broadly speaking, there are three things you might want to do with lists:
# 
# 1. add elements
# 1. remove elements
# 1. inspect elements
# 
# All of these can be done in a number of different ways. Here are a few main ones:
# 
# 1. To **add** an element, you can use `my_list.append(elem)`. To add all the elements of some other sequence at once, you can try `my_list.extend(other_seq)`. Related to that, the addition operator `+` for lists corresponds to concatenation, and the multiplication operator `*` corresponds to duplication (remember how it went for strings?)
# 1. To **remove** elements by value, you can use `my_list.remove('some_value')`, which will delete the first occurrence of that value in your list. Alternatively, you can remove elements based on their index: `del my_list[idx]` will remove the value at index `idx`; `elem = my_list.pop(idx)` will remove the value at index `idx` and place it in the variable `elem` instead.
# 1. To **access** the value at a given index `idx`, we generally use indexing: `my_value = my_list[idx]`.
# 
# Try predicting what the code below will print!

# In[ ]:


chimps = (["chimp", "peanuts"] * 3)

chimps.remove("chimp")
del chimps[1]
something = chimps.pop(-2)

# what will this print?
print(something, chimps)


# ### Slicing and unpacking
# 
# Another common type of operation with lists (or *ordered* sequences in general) is to iterate over them. This is very frequently done with **slicing**:
# 
# ```Python
# >>> daily_articles = ['no peanut', 'one peanut', 'two peanuts', 'three peanuts', 'peanuts stolen from Bond', 'evil plan to destroy Paris']
# >>> daily_articles[1:3]
# ['one peanut', 'two peanuts']
# >>> daily_articles[1:-2]
# ['one peanut', 'two peanuts', 'three peanuts']
# >>> daily_articles[::2]
# ['no peanuts', 'two peanuts', 'peanuts stolen from Bond']
# >>> daily_articles[-2::-2]
# ['peanuts stolen from Bond', 'two peanuts', 'no peanuts']
# >>> daily_articles[::-1]
# ['evil plan to destroy Paris', 'peanuts stolen from Bond', 'three peanuts', 'two peanuts', 'one peanut', 'no peanuts']
# ```
# 
# As you can see, `my_list[::-1]` traverses the list in reverse: it starts from the end. Another function you can use for that is `reversed()`.
# 
# Another very common thing to do with ordered sequence is **unpacking** them.
# ```Python
# >>> the_tribe = ["I am a chimp!", "I am a gorilla!", "I am a mandrill!", "I am tarzan!"]
# >>> chimp, gorilla, mandrill, tarzan = the_tribe
# >>> chimp
# 'I am a chimp!'
# >>> gorilla
# 'I am a gorilla!'
# >>> mandrill
# 'I am a mandrill!'
# >>> tarzan
# 'I am tarzan!'
# >>> *monkeys, weird_monkey = the_tribe
# >>> monkeys
# ['I am a chimp!', 'I am a gorilla!', 'I am a mandrill!']
# >>> weird_monkey
# 'I am tarzan!'
# >>> best, *rest, hairless  = the_tribe
# >>> best
# 'I am a chimp!'
# >>> rest
# ['I am a gorilla!', 'I am a mandrill!']
# >>> hairless
# 'I am tarzan!'
# ```
# 
# **Note:** _The "splat" operator_ `*` _allows you to group multiple elements together when unpacking. 
# You can only use that "splat" operator once per unpacking!_
# 
# #### Exercise #1: Sifting through
# 
# Using slices, write a function called `every_third(l)` that takes a list `l` as argument and returns every third element in the list.
# 
# Write a function called `first_and_last(l)` that returns a list containing only the first and last element of the argument list `l`.

# In[7]:


# write your code here
def every_third(l):
    result = l[2::3]
    return result

def first_and_last(l):
    if len(l)==0:
        result = []
    elif len(l)==1:
        result = l[:]
    else:
        result = []
        result.append(l[0])
        result.append(l[len(l)-1])
    return result


# ## Tuples
# 
# Tuples are another very frequently used data structure in python. Unlike lists, they are *immutable* ordered sequences.
# 
# As they are ordered sequences, you can use slicing, indexing and unpacking with tuples. As they are immutable, you can also use (some) tuples as dictionary keys.
# 
# Tuples are omnipresent in python code. Every time you return multiple values at once, you're in fact returning a tuple and unpacking it down the line:
# 
# ```Python
# def chimp_life(peanuts):
#     ...
#     # this is strictly equivalent to:
#     # return (chimp_action, remaining_peanuts)
#     return chimp_action, remaining_peanuts
# 
# # this is actually just unpacking!
# chimp_action, peanuts = chimp_life(peanuts)
# ```
# 
# In fact, any value followed by a comma is interpreted as a tuple:
# ```Python
# >>> chimp = 'chimp'
# >>> type(chimp)
# <class 'str'>
# >>> chimp = 'chimp',
# >>> type(chimp)
# <class 'tuple'>
# ```
# 
# You may also add parentheses around a tuple:
# ```Python
# >>> monkeys_a = 'chimps', 'mandrill'
# >>> monkeys_b = 'chimps', 'mandrill',
# >>> monkeys_c = ('chimps', 'mandrill')
# >>> monkeys_d = ('chimps', 'mandrill',)
# >>> monkeys_a == monkeys_b == monkeys_c == monkeys_d
# True
# ```
# 
# Parentheses are required when you create tuples of tuples, or when creating an empty tuple
# ```Python
# >>> monkeys_e = ('chimps', 'mandrill'),
# >>> monkeys_a == monkeys_e
# False
# >>> empty = ()
# >>> type(empty)
# <class 'tuple'>
# ```
# 
# 
# ### Exercise #2: GCD
# 
# Write a function to compute the [GCD](https://en.wikipedia.org/wiki/Greatest_common_divisor) of two positive integers. You can freely use the fact that `gcd(a, b)` is mathematically equal to `gcd(b, a % b)`, and that `gcd(a, 0) == a`.
# 
# If it helps, starts by assuming that `a >= b` if you'd like, but your final function should be able to handle all cases, including when `a < b`.
# 
# It is possible to accomplish this in three lines of Python code (or with extra cleverness, even fewer! Go and &#9971;!). Consider exploiting tuple packing and unpacking!
# 
# *Note: The standard library has a `gcd` function. Avoid simply importing that function and using it here - the goal is to practice with tuple packing and unpacking!*

# In[15]:


def gcd(a, b):
    """Compute the GCD of two positive integers."""
    if a==0 :
        return b
    if b==0:
        return a
    if a>=b:
        small = b
    else:
        small = a
        
    for i in range(1, small+1):
        if(a%i==0) and (b%i==0):
            result = i
    return result
    
gcd(10, 25) # => 5
gcd(25, 10) # => 5

gcd(14, 15) # => 1
gcd(15, 14) # => 1

gcd(3, 9) # => 3
gcd(9, 3) # => 3

gcd(1, 1) # => 1


# ## Dictionaries
# 
# Dictionaries (the `dict` type in python) are mappings that associate keys to values. 
# 
# Instead of using integers to index elements, as you would in a list, dictionaries allow you to use whatever value as a key. 
# 
# As such, you can use `del my_dict[key]` to remove a certain `key`, `value` pair from a dictionary
# 
# The only two requirements for keys are that they need to be unique and hashable, i.e., immutable and composed only of immutable objects.
# 
# You can retrieve only the keys as an ordered sequence using the `dict.keys()` method. The same thing applies for values with `dict.values()`. To get pairs of keys associated to values, you can use `dict.items()`.
# 
# ```Python
# >>> d = {'chimp': 'peanut', 'Bond': 'James'}
# >>> d.keys()
# dict_keys(['chimp', 'Bond'])
# >>> d.values()
# dict_values(['peanut', 'James'])
# >>> d.items()
# dict_items([('chimp', 'peanut'), ('Bond', 'James')])
# ```
# 
# ### Exercise #3: Flip it!
# Consider this (naive) implementation of a dictionary comprehension that swaps the keys and values in a dictionary:
# 
# ```Python
# {value: key for key, value in dictionary.items()}
# ```
# 
# This approach will fail when there are two keys in the dictionary with the same value. Why will it fail?
# 
# Write a function that properly reverses the keys and values of a dictionary - each key (originally a value) should map to a collection of values (originally keys) that mapped to it. For example,
# 
# ```Python
# flip_dict({"CA": "US", "NY": "US", "ON": "CA"})
# # => {"US": ["CA", "NY"], "CA": ["ON"]}
# ```
# 
# Note: there is a data structure in the `collections` module from the standard library called `defaultdict` which provides exactly this sort of functionality. You provide it a factory method for creating default values in the dictionary (in this case, a list.) You can read more about `defaultdict` and other `collections` data structures [here](https://docs.python.org/3/library/collections.html).

# In[37]:


def flip_dict(input_dict):
    """Reverse the keys and values of a dictionary."""
    result = {}
    for value in input_dict.values():
        new_value = [key for key in input_dict.keys() if input_dict[key] == value]
        if(len(new_value)==1):
            result[value] = new_value
        else:
            result[value] = new_value
        
    return result

flip_dict({"CA": "US", "NY": "US", "ON": "CA"})
# should print exactly {"US": ["CA", "NY"], "CA": ["ON"]}


# ### Exercise #4: Flip it again!
# 
# Write a function `merge_keys(input_dict)` that takes a `dict` as input and returns a copy of it, where keys mapping to the same value are now stored in a single tuple. For instance:
# 
# ```Python
# merge_keys({"CA": "US", "NY": "US", "ON": "CA"})
# # => {("CA", "NY"):"US", "ON": "CA"}
# ```
# In this flipped dictionary, keys can either be **strings** or **tuples of strings**.
# 
# What will happen if you flip twice a dictionary whose keys you've previously merged, using the two functions `flip_dict(input_dict)` and `merge_keys(input_dict)`?
# 

# In[46]:


def merge_keys(input_dict):
    """Merge keys to make dict more easily reversible."""
    result = {}
    for value in input_dict.values():
        new_key = tuple((key for key in input_dict.keys() if input_dict[key] == value))
        if(len(new_key)==1):
            result[new_key[0]] = value
        else:
            result[new_key] = value
    
    return result

print(merge_keys({"CA": "US", "NY": "US", "ON": "CA"}))
# should print exactly {("CA", "NY"):"US", "ON": "CA"}

# print(flip_dict(flip_dict(merge_keys({"CA": "US", "NY": "US", "ON": "CA"}))))
# print(flip_dict(merge_keys({"CA": "US", "NY": "US", "ON": "CA"})))

# what will be printed here?


# ## Comprehensions
# 
# ### Read
# 
# Predict the output of each of the following list comprehensions. After you have written down your hypothesis, run the code cell to see if you were correct. If you were incorrect, discuss with a partner why Python returns what it does.
# 
# ```Python
# [x for x in [1, 2, 3, 4]]
# [n - 2 for n in range(10)]
# [k % 10 for k in range(41) if k % 3 == 0]
# [s.lower() for s in ['PythOn', 'iS', 'cOoL'] if s[0] < s[-1]]
# 
# # Something is fishy here. Can you spot it?
# arr = [[3,2,1], ['a','b','c'], [('do',), ['re'], 'mi']]
# print([el.append(el[0] * 4) for el in arr])  # What is printed?
# print(arr)  # What is the content of `arr` at this point?
# 
# [letter for letter in "pYthON" if letter.isupper()]
# {len(w) for w in ["its", "the", "remix", "to", "ignition"]}
# ```

# In[ ]:


# Predict the output of the following comprehensions. Does the output match what you expect?
print([x for x in [1, 2, 3, 4]])
print([n - 2 for n in range(10)])
print([k % 10 for k in range(41) if k % 3 == 0])
print([s.lower() for s in ['PythOn', 'iS', 'cOoL'] if s[0] < s[-1]])

# Something is fishy here. Can you spot it?
arr = [[3,2,1], ['a','b','c'], [('do',), ['re'], 'mi']]
print([el.append(el[0] * 4) for el in arr])  # What is printed?
print(arr)  # What is the content of `arr` at this point?

print([letter for letter in "pYthON" if letter.isupper()])
print({len(w) for w in ["its", "the", "remix", "to", "ignition"]})


# ### Exercise #5: Write
# 
# Write comprehensions to transform the input data structure into the output data structure:
# 
# ```Python
# [0, 1, 2, 3] -> [1, 3, 5, 7]  # Double and add one
# ['apple', 'orange', 'pear'] -> ['A', 'O', 'P']  # Capitalize first letter
# ['apple', 'orange', 'pear'] -> ['apple', 'pear']  # Contains a 'p'
# 
# ["TA_sam", "student_poohbear", "TA_guido", "student_htiek"] -> ["sam", "guido"] # TA's names
# ['apple', 'orange', 'pear'] -> [('apple', 5), ('orange', 6), ('pear', 4)] # words and their lengths in a list of tuples
# 
# ['apple', 'orange', 'pear'] -> {'apple': 5, 'orange': 6, 'pear': 4} # words and their lengths as dictionary key-value pairs
# ```
# 
# Make sure to use the pre-defined variables!

# In[54]:


nums = [0, 1, 2, 3]
fruits = ['apple', 'orange', 'pear']
people = ["TA_sam", "student_poohbear", "TA_guido", "student_htiek"]

# Add your comprehensions here!
nums_doubled_and_incremented = [2*x+1 for x in nums] # nums -> Double and add one

fruits_capitalized_first_letter = [x.capitalize() for x in fruits] # fruits -> Capitalize first letter
fruits_cotaining_p = [x for x in fruits if 'p' in x] # fruits -> Contains a 'p'

people_TA_names = [name for name in people if name[0:2] == 'TA'] # people -> TA's names
fruits_word_and_length_tuples = [(x, len(x)) for x in fruits ] # fruits -> words and their lengths in a list of tuples

fruits_word_to_length_dict = {x:len(x) for x in fruits} # fruits -> words and their lengths as dictionary key-value pairs

# print(nums_doubled_and_incremented)
# print(fruits_capitalized_first_letter)
# print(fruits_cotaining_p)
# print(people_TA_names)
# print(fruits_word_and_length_tuples)
# print(fruits_word_to_length_dict)


# ### Exercise #6: Pascal's Triangle
# Write a function that generates the next level of [Pascal's triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle) given a list that represents a row of Pascal’s triangle.
# 
# ```Python
# generate_pascal_row([1, 2, 1]) -> [1, 3, 3, 1]
# generate_pascal_row([1, 4, 6, 4, 1]) -> [1, 5, 10, 10, 5, 1]
# generate_pascal_row([]) -> [1]
# ```
# 
# As a reminder, each element in a row of Pascal's triangle is formed by summing the two elements in the previous row directly above (to the left and right) that elements. If there is only one element directly above, we only add that one. For example, the first 5 rows of Pascal's triangle look like:
# 
# ```
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
# ```
# 
# You may find the `zip` function discussed briefly in lecture useful, along with some cleverness. Alternatively, you could solve this problem with `enumerate`. Avoid using a loop of the form `for i in len(range(row)):`.
# 
# *Hint: Check out the diagram below. How could you use this insight to help complete this problem?*
# 
# ```
#   0 1 3 3 1
# + 1 3 3 1 0
# -----------
#   1 4 6 4 1
# ``` 

# In[62]:


def generate_pascal_row(row):
    """Generate the next row of Pascal's triangle."""
    if len(row)==0:
        return [1]
    list1 = row[:]
    list2 = row[:]
    list1.insert(0, 0)
    list2.append(0)
    result = []
    for i in range(len(row)+1):
        result.append(list1[i] + list2[i])
        
    return result

generate_pascal_row([1, 2, 1])  # => [1, 3, 3, 1]
generate_pascal_row([1, 4, 6, 4, 1])  # => [1, 5, 10, 10, 5, 1]
generate_pascal_row([])  # => [1]


# #### Exercise #7: Pretty Printing Pascal (Bonus)
# 
# Given a number `n`, print out the first `n` rows of Pascal's triangle, centering each line. You should use the `generate_pascal_row` function you  wrote previously. The Pascal's triangle with 1 row just contains the number `1`.
# 
# To center a string in Python, you can use the `.center(width)` method. For example:
# 
# ```Python
# >>> 'chimp'.center(10)
# '  chimp   '
# ```
# 
# You can even specify an optional `fillchar` to fill with characters other than spaces!
# 
# The hardest part of this problem is determining the width of the bottom row of the triangle. You'll need to generate all rows of the triangle and store them before you can print any of them.

# In[81]:


def print_pascal_triangle(n):
    """Print the first n rows of Pascal's triangle."""
    result = []
    all_str = []
    for i in range(n):
        str_result = ''
        result = generate_pascal_row(result)
        for num in result:
            str_result += str(num) + ' '
        all_str.append(str_result[:-1])
        
        
    for cell in all_str:
        print(cell.center(len(all_str[n-1])))
        


# ## Even More Bonus Problems
# 
# *Only attempt to solve these bonus problems if you've finished the rest of the lab. Bonus problems are intentionally much harder than the other lab problems.*

# ### Exercise #8: Polygon Collision
# 
# Given two polygons in the form of lists of 2-tuples, determine whether the two polygons intersect.
# 
# Formally, a polygon is represented by a list of (x, y) tuples, where each (x, y) tuple is a vertex of the polygon. Edges are assumed to be between adjacent vertices in the list, and the last vertex is connected to the first. For example, the unit square would be represented by
# 
# ```
# square = [(0,0), (0,1), (1,1), (1,0)]
# ```
# 
# You can assume that the polygon described by the provided list of tuples is not self-intersecting, but do not assume that it is convex.
# 
# **Note: this is a *hard* problem. Quite hard.**

# In[86]:


def polygon_collision(poly1, poly2):
    edges_poly1 = []
    edges_poly2 = []
    
    for index in range(len(poly1)-1):
        edges_poly1.append((poly1[index+1][0]-poly1[index][0], poly1[index+1][1]-poly1[index][1]))
    edges_poly1.append((poly1[len(poly1)-1][0]-poly1[0][0], poly1[len(poly1)-1][1]-poly1[0][1]))
        
    for index in range(len(poly2)-1):
        edges_poly2.append((poly2[index+1][0]-poly2[index][0], poly2[index+1][1]-poly2[index][1]))
    edges_poly2.append((poly1[len(poly2)-1][0]-poly2[0][0], poly2[len(poly2)-1][1]-poly2[0][1]))
        
#     print(edges_poly1, edges_poly2)
    
    return True

unit_square = [(0,0), (0,1), (1,1), (1,0)]
triangle = [(0,0), (0.5,2), (1,0)]

print(polygon_collision(unit_square, triangle))  # => True


# ## Done Early?
# 
# Skim [Python’s Style Guide](https://www.python.org/dev/peps/pep-0008/), keeping the Zen of Python in mind. Feel free to skip portions of the style guide that cover material we haven't yet touched on in this class, but it's always good to start with an overview of good style.

# ## Submitting Labs
# 
# Alright, you did it! By now you should know the drill... Don't forget to submit your lab through Arche once you're done. And remember:
# 
#  1. **Convert it** to python script (`jupyter nbconvert --to script {YOUR_NOTEBOOK}.ipynb`)
#  1. **Test it** to verify it doesn't crash
#  1. **Name it** correctly so it can be automatically graded (Jane Doe's submission for this lab should be called `tp4_jane_doe.py`)
# 
# 
# *Adapted from CS41's labs.*
# 
# *They credit Puzzling.SE (specifically [JLee](https://puzzling.stackexchange.com/users/463/jlee)), ProjectEuler and InterviewCake for several problem ideas*

# > With <3 by @sredmond
# 
# > With chimps by tmickus
