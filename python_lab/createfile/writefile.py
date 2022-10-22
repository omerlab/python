############################################################
###  Python File Write
############################################################
### Write to an Existing File
### To write to an existing file, you must add a parameter to the open() function:

### "a" - Append - will append to the end of the file

### "w" - Write - will overwrite any existing content

#### Example
#### Open the file "demo.txt" and append content to the file:

# f = open("demo.txt", "a")
# f.write("Learn python is the best thing you can do for your IT carreer ")
# f.write("My new goal is to practice 2 hours every day on python")
# f.close()

#### open and read the file after the appending:

# f = open("demo.txt", "r")
# print(f.read())

####  Example
####  Open the file "demofile3.txt" and overwrite the content:
####  Note: the "w" method will overwrite the entire file.

# f = open("demo.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

####  open and read the file after the appending:

# f = open("demo.txt", "r")
# print(f.read())

###############################################################
###            Create a New File
################################################################
### To create a new file in Python, use the open() method, with one of the following parameters:

### "x" - Create - will create a file, returns an error if the file exist

### "a" - Append - will create a file if the specified file does not exist

### "w" - Write - will create a file if the specified file does not exist

### Example
### Create a file called "myfile.txt":
### Result: a new empty file is created!

f = open("math.py", "x")

### Example
### Create a new file if it does not exist:

# f = open("lambda.py", "w")


##############################################################
####         Python Delete File
##############################################################

### Delete a File
### To delete a file, you must import the OS module, and run its os.remove() function:

### Example
### Remove the file "demofile.txt":

#f = open("demofile.txt", "w")   # This will create demofile.txt

# import os
# os.remove("demofile.txt")      # will delete

### Check if File exist:
### To avoid getting an error, you might want to check if the file exists before you try to delete it:

### Example
### Check if file exists, then delete it:

# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")

####################################################
####   Delete Folder
#####################################################

# To delete an entire folder, use the os.rmdir() method:
# Note: You can only remove empty folders.
# Example
# Remove the folder "callable.py":

# import os
# os.rmdir("callable.py")
