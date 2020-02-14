import os

# Sensitive informations like credentials can be hidden in the code by using Environment variables, os.environ.get is like a dictionary
# returning key, value pair.
password=os.environ.get("my_passwd")
print(password)

#password=os.environ.get("my_passwd","Password not found")