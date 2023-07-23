#password generator
import random
import string

user_input = int(input("enter your favourite number:"))
user_input2 = input("enter your three letter favourite word:")


if not type(user_input) is int:
    raise Exception("user is requested to enter a integer data type.")
elif len(user_input2)>3:
    raise Exception("sorry, no more than 3 letters are allowed.")
else:
    print("YOUR GOOD TO GO TO GENERATE PASSWORD.")


random_string = string.ascii_letters + string.digits + string.ascii_uppercase +string.ascii_lowercase
random_word = random.choice(random_string)
a = random_string[4:10]
password = a+user_input2+random_word
print(f"your generated password is {password}")