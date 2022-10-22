#################################################################################
#####  This code will collect user's information to be authenticated
#################################################################################

USERNAME = "b"
PASSWORD = "ad"
EMAIL = "gmail"
PHONE = 443

USERNAME = input("Username: ")
PASSWORD = input("Password: ")
EMAIL = input("Email: ")
PHONE = int(input("Phone" ))
LOGIN = print(f" Username: {USERNAME} \n Password: {PASSWORD} \n Email: {EMAIL} \n Phone: {PHONE}")
print(LOGIN)
print(f" Congratulation {USERNAME} your have successfully login")
