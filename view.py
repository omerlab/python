# # Create a  function that will calculate Area
# # Value :


# lenght = 10
# width = 4
# area = lenght*width

# # We are defining a function that computes area

# def area(lenght, width):
#     a = lenght*width
#     return a 

# # Let's call the function 

# print("The Area is:", area(10, 4))


# # input is a defined function in python
# name = input("Enter your name: ")
# age = input("Please provide your age: ")
# print(f"Hello {name}, it 's nice meeting you, I am {age} too")


# #######################################################################
# # To know available function that can be used with random 

# import random
# print(dir(random))

# exple of function:
# function with this presentation:  _<function>_ are python function
#  
# ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE',
#  '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
#   '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor',
#    '_index', '_inst', '_isfinite', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt',
#     '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate',
#      'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate',
#       'randbytes', 'randint', 'random','randrange', 'sample', 'seed', 'setstate', 'shuffle',
#        'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

# # To call help option for a function 

# import random
# help(random.randint)

# exple:
# randint(a, b) method of random.Random instance
#     Return random integer in range [a, b], including both end points.

### pprint function helps to show content of what is available function that can be used with random 

# import random
# from pprint import pprint  # pprint is a module but also a function
# pprint(dir(random)) # everything will be display alphabetically

# callable object in pyton are function
# we can't call module(pprint, ) but we can call function

# import os 
# from pprint import pprint

# print(callable(pprint))

# import os 
# from pprint import pprint   # for pprint to be callable we need to import pprint function from pprint module. if not i will not work
#                             # If a function is callable we will receive True, if not False  
# print(callable(pprint))

#############################################################
#####  to know what function can be use in the module os do 
#############################################################

# import os
# print(dir(os))

# import os
# from pprint import pprint 
# print(callable(os.name))   # name will return False meaning that it cannot be call


##########################
### for the module random
# ##########################
# import random 
# print(dir(random))

##### To use the callable function to check if a function is callable do

import random 
print(callable(random.uniform))
