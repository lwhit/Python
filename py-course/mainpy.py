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

# try:
#     #input gives str input, always. Must typecast it
#     age = int(input("how old are you?: "))
#     age += 1
#     print("on your birthday you will be " + str(age) + " years old")
# except:
#     print("input must be an int")

#################### py math
# import math
# pi = math.pi
# print (pi)

# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(100))
# print(max(3,pi,4))

#################### string manipulation
# [start:stop:step]
# start inclusive, stop exclusive

# name = "jeremy mcdonald"
# try:
#     spaceIndex = name.find(' ')
#     firstName = name[:spaceIndex]
#     lastName = name[spaceIndex:]
#     print("first name:", firstName)
#     print("last name:", lastName)
#     print("name backwards: ", name[::-1])
# except:
#     print("input a name with a space")
    
################### string slicing
# slice(index of starting char (inclusive), index of ending char(exclusive) )
# website = "https://google.com"    
# webSlice = slice(8,-4)
# print("website name = " + website[webSlice])

################### if, elif, else
# age = 18
# if age >= 18:
#     print("adult")
# elif age >= 13:
#     print("teen")
# else:
#     print("child")

################### operators.. and, or, not
# temp = 109
# if temp > 0 and temp < 100:
#     print("nice day")
# elif temp < 0 and temp > -20 or False:
#     print("cold but manageable")
# elif not(temp>110):
#     print("quite hot but manageable")
# else:
#     print("quite hot")
    
################### while loop
# name = None
# while not name:
#     name = input("Enter your name: ")
# print("name is:", name)

################### for loop
# name = "Bob"
# for char in name:
#     print(char)
# for index in range(len(name)):
#     print(index)
# for i in range(9,40, len(name)):
#     print(i)

# import time
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year")

# rows = int(input("num rows: "))
# columns = int(input("num columns: "))
# for r in range(rows):
#     for c in range(columns):
#         print('# ', end="")
#     print()

#################### loop control statements
# break =     used to terminate loop 
# continue =  skips to next iteration of the loop
# pass =      does nothing, acts as placeholder

# phoneNumber = "555-123-5678"
# cleanNumber = ""
# for i in phoneNumber:
#     if i == '-':
#         continue #don't add character to cleanNumber string. "continue to next iteration"
#     cleanNumber += i
# print("clean number:", cleanNumber)

########################## DATA STRUCTURES. ##########################
# [] List. Mutable
# () Tuple. Immutable
# {} Set. Unordered, unindexed. No duplicate values
# {} Dictionary. Mutable, unordered collection of unique key:value pairs

#################### Our first data structure! LISTS
# food = ["cereal","hamburger","milk","lettuce", 2]
# # food.append("ice cream")
# # food.remove("cereal")
# # food.pop()
# # food.insert(0, "cake")
# # food.sort()
# # food.clear()
# print(food)

#################### 2D LISTS
# cereal = ["coco puffs","honey nut cheerios","lucky charms"]
# drinks = ["milk","gatorade","water"]
# food = [cereal,drinks]
# print(food[0][1])
# food = cereal + drinks
# print(food)

#################### TUPLE
# tuple = immutable, ordered collection used to group together related data

# student = ("george",25,"male")
# print(student.count("george"))
# print(student.index("george"))
# if "male" in student:
#     print("student is male")
# student[0] = "henry"  #doesn't work. Tuples are immutable
# print(student)  

#################### SET
# unordered, unindexed. No duplicates!

# utensils = {"fork","spoon","knife"}
# dishes = {"bowl","plate","cup","knife"}

# print(utensils.difference(dishes))      # {'fork','spoon'}
# print(utensils.intersection(dishes))    # {'knife'}
# print(utensils.issubset(dishes))        # False. A subset has only entries
#                                             # that the main set has
# print(utensils.issubset( {"spoon","knife","fork","butterknife"} ))  #True
# print(utensils.isdisjoint(dishes))      # returns True if the sets have no common entries
#                                             # so this returns False (knife in common)
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# dishes.update(utensils) 
# for x in utensils:
#     print(x)
    
# dinnerTable = utensils.union(dishes)    
# for x in dinnerTable:
#     print(x)

########################### Dictionary
# changable, unordered collection of unique key:value pairs
# fast because they use hashing

# capitals = {"USA":"Washington DC",
#             "India":"New Dehli",
#             "China":"Beijing",
#             "Russia":"Moscow"}
# capitals.update({"Germany":"Berlin"})   # Adds Germany:Berlin key-value pair
# capitals.update({"USA":"WA DC"})        # Updates USA capital to WA DC
# capitals.pop("China")

# country = input("Enter country name who's capital you want: ")
# if (capitals.get(country)):     # If there is no 'country' key in our dict, returns None
#     print("Capital of",country,"is",capitals.get(country))
# else: print("Capital not found")

# capitals.keys()     #returns all dict keys
# capitals.values()   #returns all dict values

# #print(capitals.items())

# for key,value in capitals.items():
#     print(key,value)

