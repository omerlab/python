# ### to import module just type "import <module_name>"
# ## module "random" and "os" helps to generate random numbers and files from our os  
# ## randint function helps to collect random interger between two number
# ## thsi function is inclusive

# import random

# r = random.randint(0, 1)

# print(r)

# ## uniforn function helps to collect random decimal number

# import random

# r = random.uniform(0, 1)

# print(r)

# ## randrange function helps to collect a random interger but we provide only one argument
# randrange(start, stop=None, step=1) method of random.Random instance
#     Choose a random item from range(start, stop[, step]).

#     This fixes the problem with randint() which includes the
#     endpoint; in Python this is usually not what you want.
# ## you can create space between random number base on 5 (1, 100, 5)

# import random

# r = random.randrange(9)

# print(r)


#### os modules is used to create and delete files and folders
## join() helps to handler / \ in python, you don't need to worry about 

import os
way = "I:\python"

### os.path.join(way, "python_lab")

folder = os.path.join(way, "python_lab", "file_handling" )

if not os.path.exists(folder):
        os.makedirs(folder)
#    os.makedirs(folder, exit_ok=True) # This will the same thing than the previous code
# os.removedirs(folder)    # will remove the folder. indentation is important 

#  To avoid error if the folder doesn't exist we use condition
# if os.path.exists(folder):    # will remove the folder is exist or will not give an error if not exist
#     os.removedirs(folder)


print(folder)
# os.makedirs(folder)
# os.mkdir(folder)

### makedirs can do that create multiple folders that don't exist
# os.makedirs(folder)

### mkdir() cannot create multiple folders that don't exist
# os.mkdir(folder)
 

#  We can create folder with mkdir by using conditions