#!/usr/bin/env python
# coding: utf-8

# # Mini-lab: getting to know classes
# 
# ## Goals of this lab
# 
# This lab session is going to be lighter, so as to give you the opportunity to ask questions on what we've covered in previous labs:
# 
# - syntax (labs 1 and 2)
# - strings (lab 3)
# - data structures (lab 4)
# - functions (lab 5)
# 
# This lab will also familiarize you with the basics of python object-oriented programming style (or "OOP" for short). The main point of this lab is to have you understand the basics of objects in python, as they are ubiquitous and very handy.
# 
# **NB1**: Unlike previous labs, we'll grade this lab by hand. *Do make sure that your submission runs without errors!*
# 
# **NB2**: For the more advanced of you in SC group 2 or TAL groups 1 & 2, the next lab should already be online. If you're done early with this lab, you can work on that next one which has a ton of extra problems to keep you busy!
# 
# ## Review #1: custom types, or "classes"
# 
# As you now know, variables in python have different types: a `str` such as `"42"` is different from an `int` such as `42`. More complex types like `list` allow you to handle more complex variables with multiple elements.
# 
# Object oriented programming allows you to extend the existing base types and define your own types. We refer to these custom types as "classes". Here's an example below:
# 

# In[23]:


class Monkey:
    """A class describing monkeys."""
    def __init__(self, monkey_species, number_of_peanuts_owned):
        self.monkey_species = monkey_species
        self.number_of_peanuts = number_of_peanuts_owned


# 
# Here, we just implemented a class `Monkey` which we'll be using to describe monkeys throughout our code.
# 
# The class contains one bound function, or a **method**, called `__init__`. This is a special method we call a **constructor**: it *creates* one monkey, using external information we pass as arguments (what species of monkey we're dealing with, how many peanuts do our monkeys have...).
# 
# Another thing of note is the `self` argument of this constructor. This refers to a specific monkey **object**, i.e., an instance of the class `Monkey`, the actual monkey being constructed here.
# 
# Having implemented the `Monkey` class, we can now represent monkeys in our code:
# 

# In[24]:


noam_chimpsky = Monkey("chimpanzee", 42)
harambe = Monkey("pirate gorilla", 1)

print(noam_chimpsky)
print(harambe)

print(noam_chimpsky.monkey_species)
print(harambe.monkey_species)

print(noam_chimpsky.number_of_peanuts)
print(harambe.number_of_peanuts)


# As you can see, we have managed to create `Monkey` objects. 
# 
# What's more, our monkeys also have specific **attributes**: they each have their species, as well as a number of peanuts. These attributes allow us to describe information regarding our objects. Different objects of the same class may have different values for the same attribute, but they all have the attribute.
# 
# ## Exercise #1: Name your monkeys
# 
# Re-implement the `Monkey` class in the cell below so that constructed monkeys also have a `name` attribute.

# In[30]:


class Monkey:
    """A class describing monkeys."""
    def __init__(self, name, monkey_species, number_of_peanuts):
        self.name = name
        self.monkey_species = monkey_species
        self.number_of_peanuts = number_of_peanuts
    

noam_chimpsky = Monkey("Noam Chimpsky", "chimpanzee", 42)
harambe = Monkey("Harambe", "pirate gorilla", 1)
print(noam_chimpsky.name)
print(harambe.name)


# ### Side-note: naming conventions
# 
# As a general rule of thumb, python classes are named in "camel case": capitalized first letters, no space. So, suppose you want to represent bad guys, then you'd name the corresponding class `BadGuy`. 
# 
# In python, variables and objects are also conventionally named in "snake case": everything in lowercase, with spaces represented by underscores `_`. Hence the `noam_chimpsky`
# 
# ## Exercise #2: Create your own class
# 
# Create a class called `Hero`. `Hero` objects should have two attributes: a `name` and a `super_power`.

# In[49]:


# your implementation of the class here!

class Hero:
    def __init__(self, name, super_power):
        self.name = name
        self.super_power = super_power
    
    def use_power(self):
        print('I\'m ' + self.name + ' and I\'m using my powers of ' +self.super_power + '!')
        
    def defeat(self, loser_badguy, mistreated_monkeys=[]):
        self.use_power()
        print('The BadGuy has been vanquished.')
        num_peanuts = loser_badguy.stolen_peanuts
        loser_badguy.stolen_peanuts = 0
        print(str(num_peanuts) + ' peanuts were retrieved.')
        
        if len(mistreated_monkeys)>=0:
            assigned = num_peanuts / len(mistreated_monkeys)
            
            for monkey in mistreated_monkeys:
                monkey.number_of_peanuts = assigned
                print(str(assigned) + ' peanuts is given to ' + monkey.name)

lucky_luke = Hero("Lucky Luke", super_power="shooting faster than his shadow")


# ## Review #2:  Bound functions, or "methods"
# 
# One very powerful aspect of objects is that we can supplement them with custom functions. This allows us to define behavior specifically for objects of our class.
# 
# One example of a method is the function `list.append(elem)`, which adds an element at the end of a list. This behavior is specific for lists, and it wouldn't make sense to have it for integers or monkeys.
# 
# Here's how we implement methods:

# In[50]:


class BadGuy:
    """A class describing the arch-nemisis of a hero!"""
    def __init__(self, name):
        self.name = name
        self.stolen_peanuts = 0
        
    def greetings(self):
        print("Welcome to my evil lair, hero!") 
        print("I am %s!" % self.name)
        print("I am so evil that I have stolen %i peanuts from random monkeys!" % self.stolen_peanuts)
        
    def steal_peanut(self, monkey_victim):
        if monkey_victim.number_of_peanuts >0:
            monkey_victim.number_of_peanuts -= 1
            self.stolen_peanuts += 1 
            print("I stolen one peanut from a monkey. "+ monkey_victim.name)
        
        if monkey_victim.number_of_peanuts <=0:
            print('The BadGuy couldn\'t steal peanuts as the monkey didn\'t have any. ' + monkey_victim.name)
            
        
dr_doom = BadGuy("Dr. Doom")
dr_doom.greetings()


# As you can see, we use the `self` argument to represent the object itself. This `self` argument gives you access to the attributes of the object itself.
# 
# **NB**: All object methods must contain this `self` argument, as the first positional argument of the method. Otherwise the python interpreter will be unable to correctly handle your code.
# 
# ## Exercise #3: With great powers come great implementations
# 
# Modify your implementation of the `Hero` class to add a method called `use_power`. When called, this method should print a message describing the hero using his super power! 
# 

# In[51]:


# Modify your implementation of the `Hero` class from exercise 2

lucky_luke = Hero("Lucky Luke", super_power="shooting faster than his shadow")
lucky_luke.use_power()
# Should print "I'm Lucky Luke and I'm using my powers of shooting faster than his shadow!"


# ## Exercise #4:  Tying it all up (Bonus)
# 
# Modify the implementation of the `BadGuy` class in review 2, to add a method called `steal_peanut`. 
# 
# - This method should have one positional argument `monkey_victim`, which should be a `Monkey ` object.
# - If the `Monkey` object owns a positive number of peanuts, then remove one peanut from it, add one to the amount of peanuts stolen by the `BadGuy` object. Print a message to describe the process.
# - If the `Monkey` has zero peanuts, print a message saying that the `BadGuy` couldn't steal peanuts as the `monkey` didn't have any.
# 
# Modify the implementation of the `Hero` class to add a method called `defeat`.
# - This method should have one positional argument `loser_badguy`, as well as one keyword argument `mistreated_monkeys`, defaulting to an empty list.
# - Start by using the hero's super-power, by calling the hero's `use_power` method.
# - Print a message stating that the `BadGuy` has been vanquished.
# - Retrieve all the peanuts stolen by the `BadGuy`: get the number of peanuts stolen by the `BadGuy`, and then set the bad guy's `stolen_peanuts` attribute to zero.
# - Print a message stating how many peanuts were retrieved.
# - If there are any victim `Monkey` in your `mistreated_monkeys`, distribute the retrieved peanuts fairly among them (all monkeys should receive the same number of peanuts), and print a custom message stating how many peanuts is given to each monkey (state the names of the monkeys!)
# 
# **You are free to decide the exact messages that you display**. 
# 
# Once you're done, uncomment the last instruction in the following cell and run it to see the story unfold!

# In[52]:


def tell_a_story():
    """Tells the great tale of a heroic cow-boy saving oppressed monkeys for the cruel Dr. Doom"""
    monkeys = [
        Monkey("Noam Chimpsky", "chimpanzee", 10),
        Monkey("Harambe", "pirate gorilla", 1),
    ]

    bad_guy = BadGuy("Dr. Doom")

    while any(m.number_of_peanuts > 0 for m in monkeys):
        for monkey in monkeys:
            bad_guy.steal_peanut(monkey)

    hero = Hero("Lucky Luke", super_power="shooting faster than his shadow")

    bad_guy.greetings()

    hero.defeat(bad_guy, mistreated_monkeys=monkeys)
    
    
# Uncomment this when you're done implementing everything
tell_a_story() 


# ## Submit your code
# 
# Submit your code on Arche. Like always:
# 
# 1. Convert your submission to a python script
#  
#      You can do so by typing `jupyter nbconvert --to script {YOUR_NOTEBOOK}.ipynb` into the command line.
#      
#      Alternatively, you can use Jupyter's interface to create your file.
#      
#      - On Jupyter Notebook, go to *File -> Download As -> Python (.py)*
#      
#      - On Jupyter Lab, go to *File -> Export Notebook As... -> Export Notebook to Executable Script*
# 2. Rename it properly: tp6_fname_lname.py
# 3. Make sure everything works without errors by running it once: `python3 tp6_fname_lname.py`
# 
# > tmickus, drowning in monkeys.

# In[ ]:




