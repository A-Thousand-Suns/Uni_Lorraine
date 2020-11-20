#!/usr/bin/env python
# coding: utf-8

# # Lab 3: Strings

# ## Overview
# 
# Welcome to your third lab! The goal for today is to familiarize you with strings (or more precisely in python, `str`). Manipulating textual data is a frequent operation in day-to-day proramming &mdash; even more so for those of you interested in NLP.
# 
# As always, remember to submit your notebook as a script once you're done!
# 
# If you're done early: &#9971; Golf your functions! Make sure not to change the function names, so as to not mess up with the automatic grading down the line.

# ## What's in a string?
# 
# Strings are inherently an ordered sequence of characters. Which is why you can iterate over a string using a for-loop, or retrieve specific characters using a slice. 
# 
# Before executing the next cell, have a guess at what the output will produce!

# In[ ]:


str_a = "I am a chimp. I love peanuts. I have a neat, though slightly old, typewriter."
for char in str_a:
    print(char)
    
print(str_a[2:-2:2])


# String objects in python actually accept a number of operators you might not expect!
# 
#  - `str_a + str_b` denotates the concatenation of the two strings `str_a` and `str_b`.
#  - `str_a * i` corresponds to the concatenation of `i` copies of the string `str_a`.
#  - `str_a % value` is the basic syntax for string formatting, which we've briefly covered in the first lab.

# ### Exercise #1: Again and again
# 
# Implement two functions, `self_mul(s, n=3)` and `self_add(s, n=3)`, that both take a `str` as argument, and return it concatenated `n` times. The first may only use the multiplication operator `*`, whereas the latter may only use the addition operator `+`.
# 
# For instance:
# 
# ```
# >>> self_add("Figaro! ", n=3)
# 'Figaro! Figaro! Figaro! '
# >>> self_mul("One! Two! ", n=2)
# 'One! Two! One! Two! '
# >>> self_add("whatever", n=42) == self_mul("whatever", n=42)
# True
# ```

# In[ ]:


def self_add(s, n=3):
    temp = ''
    for i in range(n):
        temp += s
    return temp

def self_mul(s, n=3):
    s =s * n
    return s


# ## Formatting strings
# 
# One of the neatest features of `str` values in python is the ability to format them: embed the value of some other variable within the string itself.
# 
# There is a very complete mini-language regarding string formatting, which you can read [here](https://docs.python.org/3/library/string.html#formatstrings)
# 
# In short, there are three main ways of formatting strings:
# 
# - Using the modulo operator `%`:

# In[ ]:


name = 'James'
'Hello %s, welcome to my evil lair!' % name


#  - Using the `str.format()` method:

# In[ ]:


'My name is {1}, {0} {1}'.format('James', 'Bond')


# - Referring to existing variables within a format string `f"..."`:

# In[ ]:


age = 21

# compare this:
print('I am {age} year old')
# with that:
print(f'I am {age} year old')


# Note that this barely scratches the surface! For instance the `str.format()` method also accepts keywords:

# In[20]:


print("My plan, {hero}?".format(hero=name))
print("I shall destroy {target} using {weapon}!".format(target="Paris", weapon="nut-deprived chimps"))


# ### Exercise #2: Tell me what you've got
# 
# Write a function called `dict_contents(d)` that takes as argument a dictionary `d` with `str` keys and `int` values, and lists its contents within a silly message. "Which silly message", you ask? Make sure you return the following:
# 
# ```
# >>> dict_contents({"chimps": 42, "peanuts": 0})
# "As for chimps, I've got 42, sadly. As for peanuts, I've got 0, sadly."
# ```

# In[ ]:


# write your code here
def dict_contents(d):
    print("As for chimps, I've got {one}, sadly. As for peanuts, I've got {two}, sadly.").format(one=d["chimps"], two=d["peanuts"]))
    


# ## Split and join
# 
# Two crucial functions you should know about are `str.join()` and `str.split()`.
# 
#  - `str.join()` links together a series of strings:

# In[ ]:


print("A list of bare necessities: %s." % ", ".join(["peanut", "typewriter", "peanut (important!)", "evil plans"]))

print(" love peanuts! ".join(["Monkeys", "Heroes like James Bond", "But evil blokes..."]))


#  - `str.split()` breaks down a single string into a list of strings

# In[2]:


the_obvious_truth = "Chimps are born rulers and masters at eating peanuts!"

# when given an argument, we create a new string every time we encounter the argument
strings = the_obvious_truth.split("r")
for s in strings:
    print(s)
    
# this prints an empty line
print() 

# without argument, we create a new string upon encountering white-spaces
strings = the_obvious_truth.split()
for s in strings:
    print(s)
    


# ### Exercise #3: Sifting through many words
# 
# Implement a function `every_other_word(s)` that splits its argument string on spaces, joins every other item with an underscore and returns this transformed string. For instance:
# 
# ```
# >>> every_other_word("Figaro, that's a man who loves peanuts. But what about Bond? James Bond?")
# 'Figaro,_a_who_peanuts._what_Bond?_Bond?'
# ```

# In[2]:


# write your code here
def every_other_word(s):
    time = 0
    result = ''
    for i in s.split(' '):
        if(time%2 ==1):
            result += '_'
        else:
            result += i
        time += 1
    return result


    


# ## Exercise #4: Special Words
# 
# For each of the following problems, we describe a criterion that makes a word (or phrase!) special, similarly to our "Efficient Words" from lecture.
# 
# If you are using macOS or Linux, you should have a dictionary file available at `/usr/share/dict/words`, a 2.5M text file containing over 200 thousand English words, one per line. However, we also mirrored this file [on Arche](https://arche.univ-lorraine.fr/mod/resource/view.php?id=994529), so you can download the dictionary from there.
# 
# Write the method `load_english` to load English words from this file. How many English words are there in this file? Using the Arche file, we got 102305 words.

# In[21]:


# If you downloaded words from the course website,
# change me to the path to the downloaded file.
_DICTIONARY_FILE = '/usr/share/dict/words'

def load_english():
    """Load and return a collection of english words from a file."""
    num = 0
    str_list = []
    with open(_DICTIONARY_FILE, 'r') as file:
        for i in file:
            str_list.append(i)
    return str_list

english = load_english()
print(len(english))


# ### Exercise #5: Triad Phrases
# 
# Triad words are English words for which the two smaller strings you make by extracting alternating letters both form valid words.
# 
# For example:
# 
# ![Triad Phrases](http://i.imgur.com/jGEXJWi.png)
# 
# Write a function to determine whether an entire phrase passed into a function is made of triad words. You can assume that all words are made of only alphabetic characters, and are separated by whitespace. We will consider the empty string to be an invalid English word.
# 
# ```python
# is_triad_phrase("learned theorem") # => True
# is_triad_phrase("studied theories") # => False
# is_triad_phrase("wooded agrarians") # => False
# is_triad_phrase("forrested farmers") # => False
# is_triad_phrase("schooled oriole") # => True
# is_triad_phrase("educated small bird") # => False
# is_triad_phrase("a") # => False
# is_triad_phrase("") # => False
# ```
# 
# Write a set of instructions to generate a list of all triad words. Assign this list to a variable called `all_triad_words`. How many are there? We found 2770 distinct triad words (case-insensitive).
# 
# *NB: we obtained the answers above using the dictionary on Arche. If you are using another dictionary, your answers may differ.*

# In[ ]:


def is_triad_word(word, english):
    """Return whether a word is a triad word."""
    cell_word1 = word[0::2]
    cell_word2 = word[1::2]
    if ('\n' in english[0]):
        if (cell_word1+'\n' in english) and ((cell_word2+'\n' in english)) :
            return True  
    else:
        if (cell_word1 in english) and ((cell_word2 in english)) :
            return True
        
    return False
    
def is_triad_phrase(phrase, english):
    """Return whether a phrase is composed of only triad words."""
    words = phrase.split(' ')
    for i in words:
        if not(is_triad_word(i, english)):
            return False

    return  True


# In[ ]:


all_triad_words = []

for word in english:
    if is_triad_word(word[:-1], english):
        all_triad_words.append(word)
print(len(all_triad_words))


# ### Exercise #6: Surpassing Phrases (challenge)
# 
# Surpassing words are English words for which the gap between each adjacent pair of letters strictly increases. These gaps are computed without "wrapping around" from Z to A.
# 
# For example:
# 
# ![Surpassing Phrases](http://i.imgur.com/XKiCnUc.png)
# 
# Write a function to determine whether an entire phrase passed into a function is made of surpassing words. You can assume that all words are made of only alphabetic characters, and are separated by whitespace. We will consider the empty string and a 1-character string to be valid surpassing phrases.
# 
# ```python
# is_surpassing_phrase("superb subway") # => True
# is_surpassing_phrase("excellent train") # => False
# is_surpassing_phrase("porky hogs") # => True
# is_surpassing_phrase("plump pigs") # => False
# is_surpassing_phrase("turnip fields") # => True
# is_surpassing_phrase("root vegetable lands") # => False
# is_surpassing_phrase("a") # => True
# is_surpassing_phrase("") # => True
# ```
# 
# We've provided a `character_gap` function that returns the gap between two characters. To understand how it works, you should first learn about the Python functions `ord` (one-character string to integer ordinal) and `chr` (integer ordinal to one-character string). For example:
# 
# ```python
# ord('a') # => 97
# chr(97) # => 'a'
# ```
# 
# So, in order to find the gap between `G` and `E`, we compute `abs(ord('G') - ord('E'))`, where `abs` returns the absolute value of its argument.
# 
# Write a set of instructions to generate a list of all surpassing words. Assign this list to a variable called `all_surpassing_words`. How many are there? We found 1931 distinct surpassing words.
# 
# *NB: we obtained the answers above using the dictionary on Arche. If you are using another dictionary, your answers may differ.*

# In[14]:


def character_gap(ch1, ch2):
    """Return the absolute gap between two characters."""
    return abs(ord(ch1) - ord(ch2))

def is_surpassing_word(word):
    """Return whether a word is surpassing."""
    word = word.replace('\n', '')
    if (len(word)<= 1):
        return True
    
    num0 = 0
    num1 = 0
    for i in range(len(word)-1):
        num1 = character_gap(word[i], word[i+1])
        if num1 < num0:
            return False
        num0 = num1

    return True

def is_surpassing_phrase(word):
    """Return whether a word is surpassing."""
    wrods  = word.split(' ')
    for i in wrods:
        if not (is_surpassing_word(i)):
            return False
    return  True
    


# In[15]:


all_surpassing_words = []
for word in english:
    if ('\n' in english[0]):
        if is_surpassing_word(word[:-1]):
            all_surpassing_words.append(word)
    else:
        if is_surpassing_word(word):
            all_surpassing_words.append(word)

print(len(all_surpassing_words))


# ### Exercise #7: Cyclone Phrases (challenge)
# 
# Cyclone words are English words that have a sequence of characters in alphabetical order when following a cyclic pattern. 
# 
# For example:
# 
# ![Cyclone Phrases](http://i.stack.imgur.com/4XBV3.png)
# 
# Write a function that to determine whether an entire phrase passed into a function is made of cyclone words. You can assume that all words are made of only alphabetic characters, and are separated by whitespace.
# 
# ```python
# is_cyclone_phrase("adjourned") # => True
# is_cyclone_phrase("settled") # => False
# is_cyclone_phrase("all alone at noon") # => True
# is_cyclone_phrase("by myself at twelve pm") # => False
# is_cyclone_phrase("acb") # => True
# is_cyclone_phrase("") # => True
# ```
# 
# Write a set of instructions to generate a list of all cyclone words. Assign this list to a variable called `all_cyclone_words`. How many are there? As a sanity check, we found 769 distinct cyclone words.
# 
# *NB: we obtained the answers above using the dictionary on Arche. If you are using another dictionary, your answers may differ.*

# In[22]:


def is_cyclone_word(word):
    """Return whether a word is a cyclone word."""
    word = word.replace('\n', '')
    if len(word) <=1:
        return True
    letters = []

    for i in range(int(len(word)/2)):
        letters.append(word[i])
        letters.append(word[len(word)-1-i])

    if (len(word)%2)==1:
        letters.append(word[int(len(word)/2)])
        
    tem = letters[:]
    letters.sort()
    if tem == letters:
        return True
    return False
    
def is_cyclone_phrase(word):
    """Return whether a phrase is composed only of cyclone words."""
    words = word.split(' ')
    for i in words:
        if not(is_cyclone_word(i)):
            return False
    return True


# In[24]:


all_cyclone_words = []
for word in english:   
    if is_cyclone_word(word):
        all_cyclone_words.append(word)

print(len(all_cyclone_words))


# ### Other Phrases (challenge)
# 
# On Puzzling.StackExchange, the user [JLee](https://puzzling.stackexchange.com/users/463/jlee) has come up with a ton of interesting puzzles of this form ("I call words that follow a certain rule "adjective" words"). If you like puzzles, optionally read through [these JLee puzzles](https://puzzling.stackexchange.com/search?q=%22I+call+it%22+title%3A%22what+is%22+is%3Aquestion+user%3A463) or [these other puzzles inspired by JLee](https://puzzling.stackexchange.com/search?tab=votes&q=%22what%20is%20a%22%20word%20is%3aquestion).

# ### Exercise #8: Triangle Words
# The nth term of the sequence of triangle numbers is given by 1 + 2 + ... + n = n(n+1) / 2. For example, the first ten triangle numbers are: `1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...`
# 
# By converting each letter in a word to a number corresponding to its alphabetical position (`A=1`, `B=2`, etc) and adding these values we form a word value. For example, the word value for SKY is `19 + 11 + 25 = 55` and 55 is a triangle number. If the word value is a triangle number then we shall call the word a triangle word.
# 
# Write a set of instructions to generate a list of all triangle words. Assign this list to a variable called `all_triangle_words`. How many are there? As a sanity check, we found 7548 distinct triangle words.
# 
# *NB: we obtained the answers above using the dictionary on Arche. If you are using another dictionary, your answers may differ.*
# 
# *Hint: you can use `ord(ch)` to get the integer ASCII value of a character. You can also use a dictionary to accomplish this!*

# In[32]:


def is_triangle_word(word):
    """Return whether a word is a triangle word."""
    word = word.replace('\n', '')
    sum = 0
    for tem in word:
        sum += ord(tem)-64
    for i in range(sum+1):
        if ((i*(i+1))) == sum*2:
            return True

    return False


# In[33]:


all_triangle_words = []
for word in english:
    if is_triangle_word(word):
        all_triangle_words.append(word)

print(len(all_triangle_words))


# ## Done Early?
# 
# Have a look at the [`string` module in Python](https://docs.python.org/3/library/string.html). It contains a lot of very useful things, such as lists of ascii characters. Another thing you should look into is the [unicode standard in Python](https://docs.python.org/3/howto/unicode.html).

# ## Submitting Labs
# 
# Don't forget to submit your lab through Arche once you're done. And remember:
# 
# 
#  1. **Convert it** to python script
#  1. **Test it** to verify it doesn't crash
#  1. **Name it** correctly so it can be automatically graded
# 
# *Credit to CS41 (@sredmond) for the original for all the section on special words. They credit in turn: Puzzling.SE (specifically [JLee](https://puzzling.stackexchange.com/users/463/jlee)), ProjectEuler and InterviewCake for several problem ideas*

# > With <3, by @sredmond
# 
# > With peanuts, monkeys and spies, by tmickus
