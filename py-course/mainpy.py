#import os

################# ctrl + / to comment out selection #############
# name = "meredith"

# for char in name:
#     print(char)

################# str methods

# name = "Henry"

# print(len(name))
# print(name.find("H"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count('n'))
# print(name.replace("n","r"))
# print(name)

#################### type casting
# z = "three"

# try:
#     print("z = "+ int(z))
# except:
#     print("couldn't convert")
    
#################### accepting user input
# name = input("what is your name?: ")
# print("name is " + name)

try:
    #input gives str input, always. Must typecast it
    age = int(input("how old are you?: "))
    age += 1
    print("on your birthday you will be " + str(age) + " years old")
except:
    print("input must be an int")

