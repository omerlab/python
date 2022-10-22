# list is a reserve word in python

### Add and remove from a list

# list.append(4)    # with append we can only add 1 value at the time

# list.extend([10, 30 ,45])    # with extend we can add multiple value at the time

# list.remove(1)     # helps to remove value from a list. It can only remove 1 value at the time

# list = ["user1",
#         "user2",
#         "user3",
#         "user4",
#         "user5"]

# print(list[::-3])


########################################################
#### to retrieve things from is lidt we use index

# index always start with 0 1 2 3 ...   -2 -1


# employes = ["user1", "user2", "user3", "user4", "user5"]
# results = employes.index("user2")

# print(results)     # help to have the position


###############################################################
##### count helps to know the number of occurnec in a list

# employes = ["user1", "user2", "user3", "user4", "user5", "user2"]
# results = employes.count("user2")

# print(results)     # help to have the number of occurence of user2 in the list

#######################################################################################

# employes = ["Cuser1", "Auser2", "Buser3", "Duser4", "Euser5"]
# employes.sort()      # It will sort name in the list alphabetically

# print(employes)     # help to have the sort the list. note the difference with sort, we don't need to pass result if we do so we will have an error 

###############################################################################################
 ###Reverse caractere in the list
# employes = ["Cuser1", "Auser2", "Buser3", "Duser4", "Euser5"]
# employes.reverse()      # It will reverse name in the list alphabetically

# print(employes)     # help to have the reverse the list. 

##########################################################################################
#### To remove in the list use pop

# employes = ["Cuser1", "Auser2", "Buser3", "Duser4", "Euser5"]
# #result = employes.pop(1)      # It will remove element with index(1) which is Auser2
# result = employes.pop(-1)
# print(employes)     

###########################################################################################
# To remove all the element of the list

# employes = ["Cuser1", "Auser2", "Buser3", "Duser4", "Euser5"]

# result = employes.clear()       # will clear all elemet of the list
# print(employes)     

################################################################################################

### To join elemet of the list

# employes = ["Cuser1", "Auser2", "Buser3", "Duser4", "Euser5"]
# #result = employes.pop(1)      # It will remove element with index(1) which is Auser2
# result = "".join(employes)      # we start with the element that we want to join 
# print(employes)     



age = 36
#txt = "My name is John, and I am {}"
print(f"My name is John, and I am {age}")

