#!/usr/bin/env python
# coding: utf-8

# # Labs 7 & 8: Object-Oriented Python

# ## Overview
# 
# After last time's minilab, which covered the barest of object basics, we'll be playing around with actual classes today, writing a fair chunk of code and building several classes to solve a variety of problems.
# 
# Recall these definitions to guide you through this lab:
# 
# - An *object* has identity
# - A *name* is a reference to an object
# - A *namespace* is an associative mapping from names to objects
# - An *attribute* is any name following a dot ('.')
# 
# **NB:** *Like the previous mini-lab, this lab will be corrected by hand. It is crucial that you make sure everything runs smoothly and without error before submitting your work!*

# ## Part #1 Primatology

# ### Review #1 Basic Class
# 
# Let’s create a class to represent all possible apes! To start with, our friendly apes will all have their own names, stash of nuts, last known living place, as well as whether they understand American Sign Language.
# 
# ```Python
# class Ape:
#     def __init__(self, name, nut_stash, location, speaks_asl=False):
#         self.name = name
#         self.nut_stash = nut_stash
#         self.location = location
#         self.speaks_asl = speaks_asl
# ```
# 
# Our argument `speaks_asl` will be a boolean. For now, let's have `nut_stash` be an integer, the number of nuts they have. Other arguments to this constructor will be strings.
# 
# Running the following code cell will create a class object `Ape` and print some information about it.
# 
# **Note**: *If you change the content of this class definition, you will need to re-execute the code cell for it to have any effect. Any instance objects of the old class object will not be automatically updated, so you may need to rerun instantiations of this class object as well.*

# In[94]:


class Ape:
    def __init__(self, name, nut_stash, location, speaks_asl=False):
        self.name = name
        self.nut_stash = nut_stash
        self.location = location
        self.speaks_asl = speaks_asl
        
print(Ape)
print(Ape.mro())
print(Ape.__init__)


# We create an instance of the class by instantiating the class object, supplying some arguments.
# 
# ```Python
# washoe = Ape("Washoe", 41, "Central Washington University", speaks_asl=True)
# ```
# 
# ### Exercise #1: Meet your Monkey
# 
# Print out the four attributes of the `washoe` instance object.

# In[95]:


washoe = Ape("Washoe", 41, "Central Washington University", speaks_asl=True)

print(washoe.name)  # Print out the name of washoe
print(washoe.nut_stash)  # Print out the number of nuts (nut_stash) of washoe
print(washoe.location)  # Print out the location of washoe
print(washoe.speaks_asl)  # Print out whether Washoe speaks ASL (speaks_asl)


# ### Review #2 Inheritance
# 
# Let's explore inheritance by creating a `Gorilla` class that takes two additional parameters, `job`, which should be a string, and `is_white_back` that defaults to `False`.

# In[96]:


class Gorilla(Ape):
    def __init__(self, name, nut_stash, location, job, speaks_asl=False, is_white_back=False):
        super().__init__(name, nut_stash, location, speaks_asl=False)
        self.job = job
        self.is_white_back = is_white_back


# We haven't seen the `super()` call yet, and it's mostly just magic, but it concretely lets us treat the `self` object as an instance object of the immediate superclass (as measured by MRO), so we can call the superclass's `__init__` method.
# 
# We can instantiate our new class:
# 
# ```Python
# washoe = Ape("Washoe", 41, "Central Washington University", speaks_asl=True)
# harambe = Gorilla("Harambe", 106, "Rumahoy Pirate Ship", "pirate", is_white_back=True)
# koko = Gorilla("Hanabiko", 77, "Woodside, CA", "pet owner", speaks_asl=True)
# print(harambe.job)  # => "pirate"
# print(koko.job)  # => "pet owner"
# ```
# 
# Read through the following statements and try to predict their output.
# 
# ```Python
# type(washoe)
# isinstance(washoe, Ape)
# isinstance(harambe, Ape)
# isinstance(koko, Ape)
# isinstance(koko, Gorilla)
# issubclass(koko, Gorilla)
# issubclass(Ape, Gorilla)
# type(washoe) == type(harambe)
# type(harambe) == type(koko)
# washoe == harambe
# harambe == koko
# ```

# In[97]:


washoe = Ape("Washoe", 41, "Central Washington University", speaks_asl=True)
harambe = Gorilla("Harambe", 106, "Rumahoy Pirate Ship", "pirate", is_white_back=True)
koko = Gorilla("Hanabiko", 77, "Woodside, CA", "pet owner", speaks_asl=True)

print(type(washoe))
print(isinstance(washoe, Ape))
print(isinstance(harambe, Ape))
print(isinstance(koko, Ape))
print(isinstance(koko, Gorilla))
print(issubclass(Ape, Gorilla))
print(issubclass(Gorilla, Ape))
print(type(washoe) == type(harambe))
print(type(harambe) == type(koko))
print(washoe == harambe)
print(harambe == koko)


# ### Exercise #2: Stashing nuts
# 
# Let's add more functionality to the `Ape` class!
# 
# 1. Start by creating a `Nut` class, with two attributes: `nut_type`, a string giving the type of nut (cashew, walnut, peanut...) and `is_edible`, a boolean showing whether apes can eat those, which should default to `True`.
# 2. Modify the implementation of the `Ape` class: `nut_stash` should default to an empty `list`.
# 3. Create a method `stash_nuts(*nuts)` that takes a variadic number of `Nut` objects and adds them to the ape's stash.
# 4. Create a method `has_nut(nut)` that takes the `str` name of a `Nut` and returns `True` if the `nut_stash` contains such a nut, and `False` otherwise.
# 5. (Bonus): modify your method `has_nut` so that it can accept either a `str` for the nut name, or a `Nut` directly

# In[99]:


class Nut:
    # your implementation
    def __init__(self, nut_type, is_edible=True):
        self.nut_type = nut_type
        self.is_edible = is_edible

# Copy your previous implementation of the Ape class here,
# or tweak the implementation you did in a previous cell
class Ape:
    def __init__(self, name, location, speaks_asl, nut_stash=[]):
        self.name = name
        self.nut_stash = nut_stash
        self.location = location
        self.speaks_asl = speaks_asl
        
    def stash_nuts(self, *nuts):
        for cell in nuts:
            self.nut_stash.append(cell)
            
    def has_nut(self, nut):
        if isinstance(nut, Nut):
            for cell in self.nut_stash:
                if nut.nut_type == cell.nut_type:
                    return True
                
        else:
            for cell in self.nut_stash:
                if nut == cell.nut_type :
                    return True
            
        return False
            
        
        
washoe = Ape("Washoe", "Central Washington University", speaks_asl=True)
washoe.stash_nuts(
    Nut("cashew"), 
    Nut("peanut"), 
    Nut("peanut"), 
    Nut("walnut"),
)

print(washoe.has_nut("walnut"))
# uncomment when done with bonus
print(washoe.has_nut(Nut("hazelnut")))


# ### Exercise #3: Pretty monkeys
# 
# The default printing represention python objects looks pretty dreary, and is not very informative. To overcome this, python proposes two special method names: `__str__` and `__repr__`, which both return a `str` object. Implementing any of these methods will modify how objects are represente
# 
# There is a slight semantic difference between the two methods: the `__str__` is used to find the "informal" (human-friendly) string representation of an object whereas `__repr__` is used to find the "official (computer-neurotic) string representation of an object.
# 
# Modify the implementation of the `Ape` so that they return a more friendly presentation:
# 
# ```Python
# washoe = Ape("Washoe", "Central Washington University", speaks_asl=True)
# print(washoe)
# # => should print 'Ape (name: "Washoe", 0 peanuts)'
# 
# nim = Ape("Neam Chimpsky", "Black Beauty Ranch, TX", speaks_asl=True, nut_stash=[Nut("walnut"), Nut("peanut")])
# # => should print 'Ape (name: "Neam Chimpsky", 2 peanuts)'
# ```

# In[100]:


# Copy your previous implementation of the Ape class here,
# or tweak the implementation you did in a previous cell
class Ape:
    
    def __init__(self, name, location, speaks_asl, nut_stash=[]):
        self.name = name
        self.nut_stash = nut_stash
        self.location = location
        self.speaks_asl = speaks_asl
        
    def stash_nuts(self, *nuts):
        for cell in nuts:
            self.nut_stash.append(cell)
            
    def has_nut(self, nut):
        if isinstance(nut, Nut):
            for cell in self.nut_stash:
                if nut.nut_type == cell.nut_type:
                    return True
                
        else:
            for cell in self.nut_stash:
                if nut == cell.nut_type :
                    return True
            
        return False
    
    def __str__(self):
        # in any case, make sure to implement this method!
        return "Ape (name: \"{0}\", {1} peanuts)".format(self.name, len(self.nut_stash))

washoe = Ape("Washoe", "Central Washington University", speaks_asl=True)
print(washoe)
# => should print 'Ape (name: "Washoe", 0 peanuts)'

nim = Ape("Neam Chimpsky", "Black Beauty Ranch, TX", speaks_asl=True, nut_stash=[Nut("walnut"), Nut("peanut")])
print(nim)
# => should print 'Ape (name: "Neam Chimpsky", 2 peanuts)'


# ### Exercise #4 Gorilla hierarchy
# 
# Now, we'll focus on the `Gorilla` class. We want to implement functionality to determine if one gorilla ranks higher in the pack than another. 
# 
# Higher ranking apes have stashes that contain more nuts than low-ranking gorillas. In addition, white-back gorillas rank always higher in the pack than other gorillas.
# 
# 
# ```Python
# >>> harambe = Gorilla("Harambe", "Rumahoy Pirate Ship", "pirate", is_white_back=True)
# >>> harambe.stash_nuts(*[Nut("peanut")] * 106)
# >>> koko = Gorilla("Hanabiko", "Woodside, CA", "pet owner", speaks_asl=True)
# >>> koko.stash_nuts(*[Nut("peanut")] * 77)
# >>> grodd = Gorilla("Gorilla Grodd", "Black Hole HQ", "super-villain", is_white_back=True)
# >>> grodd.stash_nuts(*[Nut("peanut")] * 42)
# >>> harambe > koko
# True
# >>> grodd > harambe
# False
# ```
# 
# To accomplish this, you will need to implement a magic method `__le__` that will add functionality to determine if a course is a prerequisite for another course. Read up on [total ordering](https://docs.python.org/3/library/functools.html#functools.total_ordering) to figure out what `__le__` should return based on the argument you pass in.
# 
# To give a few hints on how to add this piece of functionality might be implemented, consider how you might extract the actual `int` number from the course code attribute.
# 
# We'll start by implementing a `__eq__` on `Ape`s. Two apes are equivalent if they have the same name, equivalent nuts stash, and the same fluency with ASL. Location doesn't matter. 
# 
# When implementing `Ape` pack ranking, keep in mind it depends only on the size of the nut stash.
# 
# **NB:** *in order for `Gorilla` to inherit the default definitions of `__le__` and `__eq__`, we have added it here too.*
# 
# Once you've implemented a `__le__` method for all `Ape`s, we'll add our additionnal constraint that white-back `Gorilla`s rank higher in the pack. 
# 
# **NB:** *As hint for the implementation, consider the `super()` method we saw previously in Review #2.*

# In[101]:


from functools import total_ordering


# Copy your previous implementation of the Ape class here,
# or tweak the implementation you did in a previous cell
@total_ordering
class Ape:
    
    def __init__(self, name, location, speaks_asl=False, nut_stash=[]):
        self.name = name
        self.nut_stash = nut_stash
        self.location = location
        self.speaks_asl = speaks_asl
        
    def stash_nuts(self, *nuts):
        for cell in nuts:
            self.nut_stash.append(cell)
            
    def has_nut(self, nut):
        if isinstance(nut, Nut):
            for cell in self.nut_stash:
                if nut.nut_type == cell.nut_type:
                    return True
                
        else:
            for cell in self.nut_stash:
                if nut == cell.nut_type :
                    return True
            
        return False
    
    def __str__(self):
        # in any case, make sure to implement this method!
        return "Ape (name: \"{0}\", {1} peanuts)".format(self.name, len(self.nut_stash))
    
    def __le__(self, other):
        # in any case, make sure to implement this method!
        if len(self.nut_stash) <= len(other.nut_stash):
            return True
        else:
            return False
    
    def __eq__(self, other):
        # in any case, make sure to implement this method!
        if len(self.nut_stash) == len(other.nut_stash):
            return True
        else:
            return False


# Copy your previous implementation of the Gorilla class here,
# or tweak the implementation you did in a previous cell  harambe = Gorilla("Harambe", "Rumahoy Pirate Ship", "pirate", is_white_back=True)  
class Gorilla(Ape):
    def __init__(self, name, location, job,   nut_stash=[], speaks_asl=False, is_white_back=False):
        super().__init__(name,  location, nut_stash=[], speaks_asl=False)
        self.job = job
        self.is_white_back = is_white_back
        
    def __le__(self, other):
        # in any case, make sure to implement this method!
        if self.is_white_back==True and other.is_white_back==False:
            return False
        elif self.is_white_back==False and other.is_white_back==True:
            return True
        else:
            if len(self.nut_stash) <= len(other.nut_stash):
                return True
            else:
                return False
            


# #### Sorting
# 
# Now that we've written a `__le__` method and an `__eq__` method, we've implemented everything we need to speak about an "ordering" of `Gorrila`s. Using the [`functools.total_ordering` decorator](https://docs.python.org/3/library/functools.html#functools.total_ordering), decorate the class so that all of the comparison methods are implemented. You should be able to run

# In[102]:


# Let's make a few gorillas
harambe = Gorilla("Harambe", "Rumahoy Pirate Ship", "pirate", is_white_back=True)
harambe.stash_nuts(*[Nut("peanut")] * 106)

koko = Gorilla("Hanabiko", 77, "Woodside, CA", "pet owner", speaks_asl=True)
koko.stash_nuts(*[Nut("peanut")] * 77)

grodd = Gorilla("Gorilla Grodd", 42, "Black Hole HQ", "super-villain", is_white_back=True)
grodd.stash_nuts(*[Nut("peanut")] * 42)

gorillas = [harambe, koko, grodd]
gorillas.sort()
print(gorillas) # => [koko, grodd, harambe]


# ### Review #3 Static & class methods
# 
# Sometimes, you have a piece of code that doesn't really belong to the object, but definitely belongs to the class.
# 
# We use static and class methods in this case. 
# 
# ```Python
# import random
# 
# class Ape:
# 
#     # some class code
#     
#     @classmethod
#     def invent_random_ape(cls):
#         name = random.choice([
#             "Kanzi",
#             "Chantek",
#             "Panzee",
#         ])
#         location = random.choice([
#             "Jungle",
#             "Zoo", 
#             "ASL research lab",
#         ])
#         speaks_asl = random.choice([
#             True,
#             False,
#         ])
#         return cls(name, location, speaks_asl=speaks_asl)
#     
#     @staticmethod
#     def monkey_around():
#         """Tell a monkey joke to lighten the mood."""
#        joke = random.choice([
#            "What do monkeys do for laughs? They tell jokes about people.",
#            "All the monkeys from these labs are real!",
#            "What kind of key unlocks a banana? A mon-key.",
#        ]) 
#        print(joke)
#        
#     # some more class code
# 
# print(Ape.invent_random_ape()) #=> Ape (name: "Chantek", 0 peanuts)
# print(Ape.monkey_around()) #=> "What kind of key unlocks a banana? A mon-key."
# ```
# 
# We use specific decorators (starting with `@`) to distinguish which methods are bound to objects, and which are static methods or class method. 
# 
# - Classmethods have a first positional argument called `cls`, representing the class itself (here `Ape`), instead of a `self` (which represent the object instance). You can use that `cls` argument to retrieve the class constructor, for instance.
# - Note that static methods do not have a positional `self` or `cls` argument. They are just semantically tied to the class, and syntactically they share the same namespace.
# 
# 
# ### Exercise #5: Much ado about peanuts
# 
# We'll create a static method `nut_inventory(*monkeys)` that takes a variadic number of monkeys as positional arguments, and returns an inventory of all the nuts they have collectively stashed. The inventory should be a python `dict`, mapping nut types to the number of corresponding nuts.
# 
# **Bonus:** Use the [`Counter` object from the collections library](https://docs.python.org/3/library/collections.html#collections.Counter) to do your inventory. Use `Nut`objects directly as keys. You will most certainly need to have a look at the magic functions [`__hash__` and `__eq__`](https://docs.python.org/3/reference/datamodel.html#object.__hash__).

# In[103]:


# If you're doing the bonus part:
# Copy your previous implementation of the Nut class here,
# or tweak the implementation you did in a previous cell.
class Nut:
    # your implementation
    def __init__(self, nut_type, is_edible=True):
        self.nut_type = nut_type
        self.is_edible = is_edible

# Copy your previous implementation of the Ape class here,
# or tweak the implementation you did in a previous cell
@total_ordering
class Ape:
    
    def __init__(self, name, location, speaks_asl=False, nut_stash=[]):
        self.name = name
        self.nut_stash = nut_stash
        self.location = location
        self.speaks_asl = speaks_asl
        
    def stash_nuts(self, *nuts):
        for cell in nuts:
            self.nut_stash.append(cell)
            
    def has_nut(self, nut):
        if isinstance(nut, Nut):
            for cell in self.nut_stash:
                if nut.nut_type == cell.nut_type:
                    return True
                
        else:
            for cell in self.nut_stash:
                if nut == cell.nut_type :
                    return True
            
        return False
    
    def __str__(self):
        # in any case, make sure to implement this method!
        return "Ape (name: \"{0}\", {1} peanuts)".format(self.name, len(self.nut_stash))
    
    def __le__(self, other):
        # in any case, make sure to implement this method!
        if len(self.nut_stash) <= len(other.nut_stash):
            return True
        else:
            return False
    
    def __eq__(self, other):
        # in any case, make sure to implement this method!
        if len(self.nut_stash) == len(other.nut_stash):
            return True
        else:
            return False
        
    @staticmethod 
    def nut_inventory(self, *monkeys):
        result = dict()
        for monkey in monkeys:
            for nut in monkey.nut_stash:
                if(bool(result.get(nut.nut_type))):
                    result[nut.nut_type] +=1
                else:
                    result[nut.nut_type] =1
        return result
    


# ## Part #2 Concrete Object Oriented Programming

# Enough monkeying around! Let's have you work on a number of objects that you may one day encounter in your programmer life.
# 
# ### Exercise #6 Not-so-SimpleGraph
# 
# In this part, you'll build the implementation for a `SimpleGraph` class in Python.
# 
# You will need to define a `Vertex` class, an `Edge` class, and a `SimpleGraph` class. The specification is as follows:
# 
# A `Vertex` has attributes:
# 
# * `name`, a string representing the label of the vertex.
# * `edges`, a set representing edges outbound from this vertex to its neighbors
# 
# A new Vertex should be initialized with an optional `name`, which defaults to `""`, and should be initialized with an empty edge set.
# 
# An `Edge` has attributes:
# 
# * `start`, a `Vertex` representing the start point of the edge.
# * `end`, a `Vertex` representing the end point of the edge.
# * `cost`, a `float` (used for graph algorithms) representing the weight of the edge.
# * `visited`, a `bool` (used for graph algorithms) representing whether this edge has been visited before.
# 
# Note that for our purposes, an `Edge` is directed: the edge from `v_a` to `v_b` is distinct from the edge from `v_b` to `v_a`.
# 
# An `Edge` requires a `start` and `end` vertex in order to be instantiated. `cost` should default to 1, and `visited` should default to `False`, but both should be able to be set via an initializer.
# 
# A `SimpleGraph` has attributes
# 
# * `verts`, a collection of `Vertex`s (you need to decide the collection type)
# * `edges`, a collection of `Edge`s (you need to decide the collection type)
# 
# as well as several methods:
# 
# * `graph.add_vertex(v)`
# * `graph.add_edge(v_1, v_2)`
# * `graph.contains_vertex(v)`
# * `graph.contains_edge(v_1, v_2)`
# * `graph.get_neighbors(v)`
# * `graph.is_empty()`
# * `graph.size()`
# * `graph.remove_vertex(v)`
# * `graph.remove_edge(v_1, v_2)`
# * `graph.is_neighbor(v1, v2)`
# * `graph.is_reachable(v1, v2)  # Use any algorithm you like`
# * `graph.clear_all()`
# 
# The actual implementation details are up to you.
# 
# *Note: debugging will be significantly easier if you write `__str__` or `__repr__` methods on your custom classes.*

# In[104]:


class Vertex:
    def __init__(self, name="", edges=set()):
        self.name = name
        self.edges = edges
        
    def __eq__(self, other):
        if self.name == other.name and self.edges == other.edges:
            return True
        else:
            return False

class Edge:
    def __init__(self, start, end, cost=1.0, visited=False):
        self.start = start
        self.end = end
        self.cost = cost
        self.visited = visited
        
    def __eq__(self, other):
        if self.start==other.start and self.end==other.end and self.cost==other.cost and self.visited==other.visited:
            return True
        else:
            return False

class SimpleGraph:
    def __init__(self, verts=[], edges=[]):
        self.verts = verts
        self.edges = edges
        
    def add_vertex(self, v):
        self.verts.append(v)
    
    def add_edge(self, v_1, v_2):
        self.edges.append(Edge(v_1,v_2))
    
    def contains_vertex(self, v):
        if v in self.verts:
            return True
        else:
            return False
    
    def contains_edge(self, v_1, v_2):
        e = Edge(v_1, v_2)
        if e in self.edges:
            return True
        else:
            return False
    
    def get_neighbors(self, v):
        pass
    
    def is_empty(self):
        if len(self.edges)==0:
            return True
        else:
            return False
    
    def size(self):
        pass
        
    def remove_vertex(self, v):
        pass
    
    def remove_edge(self, v_1, v_2):
        pass
    
    def is_neighbor(self, v1, v2):
        pass
    
    def is_reachable(self, v1, v2):
        pass
    
    def clear_all(self):
        self.verts = []
        self.edges = []


# ### Exercise #7: Implementing Graph Algorithms (bonus)
# 
# If you're feeling up to the challenge, and you have sufficient time, goimplement other graph algorithms, using your SimpleGraph from exercise #6. The point isn't to check whether you know your graph algorithms - rather, these algorithms will serve to test the correctness of your graph implementation. The particulars are up to you.
# 
# As some suggestions:
# 
# * [Longest path](https://en.wikipedia.org/wiki/Longest_path_problem)
# * [Dijkstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
# * [A*](https://en.wikipedia.org/wiki/A*_search_algorithm)
# * [Max Flow](https://en.wikipedia.org/wiki/Maximum_flow_problem)
# * <a href="https://en.wikipedia.org/wiki/Clique_(graph_theory)">K-Clique</a>
# * <a href="https://en.wikipedia.org/wiki/Component_(graph_theory)">Largest Connected Component</a>
# * [is_bipartite](https://en.wikipedia.org/wiki/Bipartite_graph#Testing_bipartiteness)
# * [hamiltonian_path_exists](https://en.wikipedia.org/wiki/Hamiltonian_path)
# 

# ### Exercise #8: My Magical Graph (bonus)
# 
# See if you can rewrite the `SimpleGraph` class from exercise #6, using magic methods to emulate the behavior and operators of standard Python. In particular,
# 
# ```
# graph[v]  # returns neighbors of v
# graph[v] = v_2  # Insert an edge from v to v2
# len(graph)
# # etc
# ```
# 
# If you've tackled exercise #6, make sure to modify your code there as well!
# 

# ### Exercise #9: Timed Key-Value Store (Bonus)
# 
# Let's build an interesting data structure straight out of an interview programming challenge from [Stripe](https://stripe.com/). This is more of an algorithms challenge than a Python challenge, but we hope you're still interested in tackling it.
# 
# At a high-level, we'll be building a key-value store (think `dict` or Java's `HashMap`) that has a `get` method that takes an optional second parameter as a `time` object in Python to return the most recent value before that period in time. If no key-value pair was added to the map before that period in time, return `None`. We'll call this class `TimedKVStore`.
# 
# You’ll need some sort of `time` object to track when key-value pairs are getting added to this map. Consider using [the `time` module](https://docs.python.org/3/library/time.html).
# 
# To give you an idea of how this class works, this is what should happen after you implement `TimedKVStore`.
# 
# ```Python
# d = TimedKVStore()
# t0 = time.time()
# d.put("1", 1)
# t1 = time.time()
# d.put("1", 1.1)
# d.get("1")  # => 1.1
# d.get("1", t1)  # => 1
# d.get("1", t0)  # => None
# ```

# In[105]:


class TimedKVStore:
    pass

d = TimedKVStore()
t0 = time.time()
d.put("1", 1)
t1 = time.time()
d.put("1", 1.1)
print(d.get("1"))  # => 1.1
print(d.get("1", t1))  # => 1
print(d.get("1", t0))  # => None


# ### Exercise #10: Remove (bonus)
# 
# Implement a method on a `TimedKVStore` to `remove(key)` that takes a key and removes that entire key from the key-value store.
# 
# Write another `remove(key, time)` method that takes a key and removes all memory of values before that time method.

# ## Part #3 Magic Methods

# ### Reading
# 
# Python provides an enormous number of special "magic" methods that a class can override to interoperator with builtin Python operations. You can skim through an [approximate visual list](http://diveintopython3.problemsolving.io/special-method-names.html) from Dive into Python3, or a [more verbose explanation](https://rszalski.github.io/magicmethods/), or the [complete Python documentation](https://docs.python.org/3/reference/datamodel.html#specialnames) on special methods. 
# 
# Fair warning, there are a lot of them, so it's probably better to skim than to really take a deep dive, unless you're loving this stuff. It's still a good thing to have a general idea of what exists and what can be done.

# ### Exercise #11: Polynomial Class
# 
# We will write a `Polynomial` class that acts like a number. As a a reminder, a [polynomial](https://en.wikipedia.org/wiki/Polynomial) is a mathematical object that looks like $1 + x + x^2$ or $4 - 10x + x^3$ or $-4 - 2x^{10}$. A mathematical polynomial can be evaluated at a given value of $x$. For example, if $f(x) = 1 + x + x^2$, then $f(5) = 1 + 5 + 5^2 = 1 + 5 + 25 = 31$.
# 
# Polynomials are also added componentwise: If $f(x) = 1 + 4x + 4x^3$ and $g(x) = 2 + 3x^2 + 5x^3$, then $(f + g)(x) = (1 + 2) + 4x + 3x^2 + (4 + 5)x^3 = 3 + 4 + 3x^2 + 9x^3$.
# 
# Construct a polynomial with variadic coefficients keywords: the zeroth coefficient is given with `c_0`, the square coefficient is given with `c_2`, and so on. For example, `f = Polynomial(c_0=1, c_2=3, c_4=5)` should construct a `Polynomial` representing $1 + 3x^2 + 5x^4$.
# 
# You will need to override the addition special method (`__add__`) and the callable special method (`__call__`).
# 
# You should be able to emulate the following code:
# 
# ```Python
# f = Polynomial(c_0=1, c_1=5, c_2=10)
# g = Polynomial(c_0=1, c_1=3, c_2=5)
# 
# print(f(5))  # => Invokes `f.__call__(5)`
# print(g(2))  # => Invokes `g.__call__(2)`
# 
# h = f + g    # => Invokes `f.__add__(g)`
# print(h(3))  # => Invokes `h.__call__(3)`
# ```
# 
# Lastly, implement a method to convert a `Polynomial` to an informal string representation. For example, the polynomial `Polynomial(1, 3, 5)` should be represented by the string `"1 * x^0 + 3 * x^1 + 5 * x^2"`.

# In[106]:


class Polynomial:
    def __init__(self, c_0, c_1, c_2):
        self.c_0 = c_0
        self.c_1 = c_1
        self.c_2 = c_2
    
    def __call__(self, x): 
        """Implement `self(x)`."""
        return self.c_0 + self.c_1*(x*x) + self.c_2*(x*x*x*x)
    
    def __add__(self, other):
        """Implement `self + other`."""
        return Polynomial(self.c_0+other.c_0, self.c_1+other.c_1, self.c_2+other.c_2)
    
    def __str__(self):
        """Implement `str(x)`."""
        print("{0} * x^0 + {1} * x^1 + {2} * x^2".format(self.c_0, self.c_1, self.c_2))


# ### Exercise #12: Polynomial Extensions (Bonus)
# 
# If you are looking for more, implement additional operations on our `Polynomial` class from exercise #11. You may want to implement `__sub__`, `__mul__`, and `__div__`.
# 
# You can also implement more complicated mathematical operations, such as `f.derivative()`, which returns a new function that is the derivative of `f`, or `.zeros()`, which returns a collection of the function's zeros.
# 
# If you need even more, write a `classmethod` to construct a polynomial from a string representation of it. You should be able to write:
# 
# ```
# f = Polynomial.parse("1 * x^0 + 3 * x^1 + 5 * x^2")
# ```

# ### Exercise #13: `MultivariatePolynomial` (Bonus)
# 
# Write a class called `MultivariatePolynomial` that represents a polynomial in many variables. For example, $f(x, y, z) = 4xy + 10x^2z - 5x^3yz + y^4z^3$ is a polynomial in three variables.
# 
# How would you provide coefficients to the constructor? How would you define the arguments to the callable? How would you implement the mathematical operations efficiently?
# 
# You should keep in mind the `Polynomial` class from exercise #11.

# In[107]:


# your implementation here
class MultivariatePolynomial:
    pass


# ## Part #4: Review: Functions as objects
# 
# As you know from class, everything in Python is an object. Including functions. Functions have some interesting attributes to explore. We'll poke around several of these attributes more in depth here. You already saw a couple of attributes in lab5, such as `__doc__`.
# 
# Usually, this information isn't particularly useful for practitioners (you'll rarely want to hack around with the internals of functions), but even seeing that you *can* in Python is very cool. And it *will* be useful on the event you *really* need to monkeypatch a given functionality. 
# 
# In this section, there is no code to write. Instead, you will be reading and running code and observing the output. Nevertheless, we encourage you to play around with the code cells to experiment and explore on your own.

# #### Default Values (`__defaults__` and `__kwdefaults__`)
# 
# As stated earlier, any default values (either normal default arguments or the keyword-only default arguments that follow a variadic positional argument parameter) are bound to the function object at the time of function definition. Consider our `all_together` function from earlier, and run the following code. Why might the `__defaults__` attribute be a tuple, but the `__kwdefaults__` attribute be a dictionary?

# In[108]:


def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options): 
    pass

all_together.__defaults__  # => (1, )
all_together.__kwdefaults__  # => {'indent':True, 'spaces':4}


# #### Code Object (`__code__`)
# 
# In CPython, the reference implementation of Python used by many people (including us), functions are byte-compiled into executable Python code, or _bytecode_, when defined. This code object, which represents the bytecode and some administrative information, is bound to the `__code__` attribute, and has a ton of interesting properties, best illustrated by example. Code objects are immutable and contain no references to immutable objects.
# 
# ```Python
# def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options):
#     """A useless comment"""
#     print(x + y * z)
#     print(sum(nums))
#     for k, v in options.items():
#         if indent:
#             print("{}\t{}".format(k, v))
#         else:
#             print("{}{}{}".format(k, " " * spaces, v))
#             
# code = all_together.__code__
# ```
# 
# | Attribute  | Sample Value | Explanation |
# | --- | --- | --- |
# | `code.co_argcount` | `3` | number of positional arguments (including arguments with default values) |
# | `code.co_cellvars` | `()` | tuple containing the names of local variables that are referenced by nested functions |
# | `code.co_code` | `b't\x00\x00...\x04S\x00'` | string representing the sequence of bytecode instructions |
# | `code.co_consts` | `('A useless comment', '{}\t{}', '{}{}{}', ' ', None)` | tuple containing the literals used by the bytecode - our `None` is from the implicit `return None` at the end |
# | `code.co_filename` | `filename` or `<stdin>` or `<ipython-input-#-xxx>` | file in which the function was defined |
# | `code.co_firstlineno` | `1` | line of the file the first line of the function appears |
# | `code.co_flags` | `79` | AND of compiler-specific binary flags whose internal meaning is (mostly) opaque to us |
# | `code.co_freevars` | `()` | tuple containing the names of free variables |
# | `code.co_kwonlyargcount` | `2` | number of keyword-only arguments |
# | `code.co_lnotab` | `b'\x00\x02\x10\x01\x0c\x01\x12\x01\x04\x01\x12\x02'` | string encoding the mapping from bytecode offsets to line numbers |
# | `code.co_name` | `"all_together"` | the function name  |
# | `code.co_names` | `('print', 'sum', 'items', 'format')` | tuple containing the names used by the bytecode |
# | `code.co_nlocals` | `9` | number of local variables used by the function (including arguments) |
# | `code.co_stacksize` | `7` | required stack size (including local variables) |
# | `code.co_varnames` | `('x', 'y', 'z', 'indent', 'spaces', 'nums', 'options', 'k', 'v')` | tuple containing the names of the local variables (starting with the argument names) |
# 
# More info on this, and on all types in Python, can be found at the [data model reference](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy). For code objects, you have to scroll down to "Internal Types."

# In[109]:


def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options):
    """A useless comment"""
    print(x + y * z)
    print(sum(nums))
    for k, v in options.items():
        if indent:
            print("{}\t{}".format(k, v))
        else:
            print("{}{}{}".format(k, " " * spaces, v))
            
code = all_together.__code__

print(code.co_argcount)
print(code.co_cellvars)
print(code.co_code)
print(code.co_consts)
print(code.co_filename)
print(code.co_firstlineno)
print(code.co_flags)
print(code.co_freevars)
print(code.co_kwonlyargcount)
print(code.co_lnotab)
print(code.co_name)
print(code.co_names)
print(code.co_nlocals)
print(code.co_stacksize)
print(code.co_varnames)


# ##### Security
# 
# As we briefly mentioned in class, this can lead to a pretty glaring security vulnerability. Namely, the code object on a given function can be hot-swapped for the code object of another (perhaps malicious function) at runtime!

# In[110]:


def nice(): print("You're awesome!")
def mean(): print("You're... not awesome. OOOOH")

# Overwrite the code object for nice
nice.__code__ = mean.__code__

print(nice())  # prints "You're... not awesome. OOOOH"


# ##### `dis` module
# 
# The `dis` module, for "disassemble," exports a `dis` function that allows us to disassemble Python byte code (at least, for Python distributions implemented in CPython for existing versions). The disassembled code isn't exactly normal assembly code, but rather is a specialized Python syntax
# 
# ```Python
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
#     
# import dis
# dis.dis(gcd)
# """
#   2           0 SETUP_LOOP              27 (to 30)
#         >>    3 LOAD_FAST                1 (b)
#               6 POP_JUMP_IF_FALSE       29
# 
#   3           9 LOAD_FAST                1 (b)
#              12 LOAD_FAST                0 (a)
#              15 LOAD_FAST                1 (b)
#              18 BINARY_MODULO
#              19 ROT_TWO
#              20 STORE_FAST               0 (a)
#              23 STORE_FAST               1 (b)
#              26 JUMP_ABSOLUTE            3
#         >>   29 POP_BLOCK
# 
#   4     >>   30 LOAD_FAST                0 (a)
#              33 RETURN_VALUE
# """
# ```
# 
# Details on the instructions themselves can be found [here](https://docs.python.org/3/library/dis.html#python-bytecode-instructions).
# You can read more about the `dis` module [here](https://docs.python.org/3/library/dis.html).

# In[111]:


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
import dis
dis.dis(gcd)


# #### Call (`__call__`)
# 
# All Python functions have a `__call__` attribute, which is the actual object called when you use parentheses to "call" a function. That is,

# In[112]:


def greet(): print("Hello world!")

greet() # "Hello world!"
# is just syntactic sugar for
greet.__call__()  # "Hello world!"


# This means that any object (including instances of custom classes) with a `__call__` method can use the parenthesized function call syntax. Which is why we wrote the following to construct a callable `Polynomial` class:
# 
# ```Python
# class Polynomial:
#     def __init__(self, coeffs):
#         """Store the coefficients..."""
#         
#     def __call__(self, x):
#         """Compute f(x)..."""
# 
# 
# # The polynomial f(x) = 4 + 4 * x + 4 * x ** 2
# f = Polynomial(4, 4, 1)
# f(5)  # Really, this is f.__call__(5)
# ```

# #### Name Information (`__module__`, `__name__`, and `__qualname__`)
# 
# Python functions also store some name information about a function, generally for the purposes of friendly printing.
# 
# `__module__` refers to the module that was active at the time the function was defined. Any functions defined in the interactive interpreter, or run as as a script, will have `__module__ == '__main__'`, but imported modules will have their `__module__` attribute set to the module name. For example, `math.sqrt.__module__` is `"math"`.
# 
# `__name__` is the function's name. Nothing special here.
# 
# `__qualname__`, which stands for "qualified name," only differs from `__name__` when you're dealing with nested functions, which we'll talk about more Week 4.
# 

# ## Submit your code
# 
# Well done making it to the end!
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
# 3. Make sure everything works without errors by running it once: `python3 tp7_fname_lname.py`

# > Stolen from CS Stanford. With <3 by @sredmond
# 
# > Adapted with gorillas by tmickus

# In[ ]:





# In[ ]:




