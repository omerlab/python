# #### os modules is used to create and delete files and folders
# ## join() helps to handler / \ in python, you don't need to worry about 

# import os
# way = "I:\python"

# ### os.path.join(way, "python_lab")

# folder = os.path.join(way, "python_lab", "test")

# if not os.path.exists(folder):
#     os.makedirs(folder)



# #    os.makedirs(folder, exit_ok=True) # This will the same thing than the previous code
# # os.removedirs(folder)    # will remove the folder. indentation is important 

# #  To avoid error if the folder doesn't exist we use condition
# # if os.path.exists(folder):    # will remove the folder is exist or will not give an error if not exist
# #     os.removedirs(folder)


# print(folder)
# # os.makedirs(folder)
# # os.mkdir(folder)

# ### makedirs can do that create multiple folders that don't exist
# # os.makedirs(folder)

# ### mkdir() cannot create multiple folders that don't exist
# # os.mkdir(folder)
 

# #  We can create folder with mkdir by using conditions

##############################################################################
######  Read a file
##############################################################################
##### File is in the pwd

# f = open("view.py", "r")
# print(f.read())

#### if The File is in a different directory, add the path to the file

# f = open("i:\\txt.txt", "r")
# print(f.read())

###### Read Only Parts of the File read(3) will read only the number of character you specify 

# f = open("view.py", "r")
# print(f.read(5))

### Read Lines
### You can return one line by using the readline() method:
### By calling readline() two times, you can read the two first lines:

# f = open("view.py", "r")
# print(f.readline())
# print(f.readline())

### By looping through the lines of the file, you can read the whole file, line by line:

# f = open("view.py", "r")
# for x in f:
#   print(x)

### Close Files
### It is a good practice to always close the file when you are done with it.

from os import lseek


f = open("demo.txt", "r")
print(f.readline())
f.close()ls