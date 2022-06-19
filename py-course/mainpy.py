#################################################################
# All code derived from "Bro Code" Youtube course, "Python Full Course - Learn to code today"
#################################################################

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

####################### Functions
# def hello(first_name, last_name, age):
#     print("hello",first_name,last_name)
#     print("you are",str(age),"years old")
    

# def goodbye():
#     hello("first","last",20)
#     print("bye")
    
# hello("Logan","W",28)
# goodbye()

####################### keyword arguments
# arguments preceded by an identifier when passed to a function
# the order of the arguments doesn't matter

# def hello(first,middle,last):
#     print("hello",first,middle,last)

# hello(last="W",first="Logan",middle="r")

###################### Scope
# scope is the region that a variable is recognized
# a variable is only available from inside the region it is created
# a global and locally scoped version of a varible can be created

# name = "Logan"  #global variable
# def display_name():
#     name = "NOT LOGAN"  #local scope --- available only inside the function
#     print(name)
    
# display_name()
# print(name)

###################### *args
# *args = parameter that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments

# def addAll(*toAdd):     # input passed as a tuple (immutable). If we want to modify this input,
#                             # we need to cast the tuple as a list []
#     sum=0
#     for i in toAdd:
#         sum += i
#     print("sum =", sum)
#     return sum

# print(addAll(5,10,15,20,25,30))

###################### **kwargs    .... keyword arguments
# **kwargs = parameter that will pack all arguments into a dictionary
#   which is useful so that a function can accept a varying amount of keyword args

# def hello(**kwargs):
#     print("hello",kwargs['first'],kwargs['last'])   #this can throw exceptions. Better to use get
#     print("hello",kwargs.get("first"),kwargs.get("LAST"))
#     for key,value in kwargs.items():
#         print(value, end=" ")
        
# hello(title="Mr.",first="Logan",middle="r",last="w")

####################### str formatting

# animal = "cow"
# item = "moon"
# print("The {} jumped over the {}".format(animal,item))
# print("The {0} jumped over the {1}".format(animal,item))      # positional arguments
# print("The {whodidit} jumped over the {thewhat}".format(whodidit=animal,thewhat=item)) 
# # ^ keyword argument
# text = "Close the {} or we're all going to {}!"
# print(text.format("door","freeze"))

# padding. number in {} is how many spaces you get to show the data. 
# {:number} will not truncate the data you're passing in
# print("My name is {:10}. Nice to meet you".format("Logan")) #10 spaces to show name
# # alignment. Left alignment: {:<10}
# #            Right alignment: {:>10}
# #            Center data: {^10}
# print("My name is {:>10}. Nice to meet you".format("Logan"))
# print("My name is {:^10}. Nice to meet you".format("Logan"))
# # formatting with keywords.. just put the keyword before the :
# animal = "dog"
# print("I have a {typeofAnimal:^15}!! Wow she's great".format(typeofAnimal=animal))

# number = 1000
# print("The number is {:.3f}".format(3.14159))   # 3.142         3 decimal figures -- this rounds our input
# print("The number is {:,}".format(number))      # 1,000
# print("The number is {:b}".format(number))      # 1111101000    binary
# print("The number is {:o}".format(number))      # 1750          octal
# print("The number is {:X}".format(number))      # 3E8           hex
# print("The number is {:E}".format(number))      # 1.000000E +03 scientific

######################## random  library
# import random

# x = random.randint(1,6)     # pseudo-random int in range [min,max]
# y = random.random()         # pseudo-random float in range [0,1)
# print(y)

# myList = ['rock','paper','scissor']
# z = random.choice(myList)
# print(z)

# cards = [1,2,3,4,5,6,7,8,9,"j","q","k","a"]
# random.shuffle(cards)
# print(cards)

######################## try-exception blocks
# try:
#     numerator=int(input("enter a number to divide: "))
#     denominator = int(input("enter a number to divide by: "))
#     result = numerator/denominator
# except ZeroDivisionError as e:
#     print(e)
#     print("You can't divide by zero")
# except ValueError as e:
#     print(e)
#     print("Enter only numbers")
# except Exception:               # having only this except block is bad practice.
#                                 # we want to know what went wrong!
#                                 # Use this block to catch anything else we didn't anticipate
#     print("something went wrong")
# else:           # no exceptions
#     print("this will run if there are no exceptions")
#     print(result)
# finally:        # Good opportunity to close a file if we opened it earlier
#                 # finally block always runs
#     print("this always runs")
    
########################### Working with files
# import os

# path = ".\jupyter.ipynb"
# path = "..\py-course"
# path = "C:\\Users\\lwhit\\OneDrive"      # double backslashes, since \ is escape operator

# if os.path.exists(path):
#     print("that location exists")
#     if os.path.isfile(path):
#         print("that's a file")
#     elif os.path.isdir(path):
#         print("that's a dir")
# else:
#     print("that location doesn't exist")

### Reading files
# I created test.txt in this folder for this part

# try:
#     with open('test.txt') as file:
#       print(file.read())
# except FileNotFoundError:
#     print("That file was not found")
    
# else:   #no exceptions thrown -- file WAS found
#     if not file.closed:
#         print("closing file")
#         file.close()
        
### Writing files
# text = "File information\nThis is some text\n"
# moreText = "Appending to file"

# try:
#     with open('test.txt','w') as file:  #overwrites text file
#         file.write(text)
# except FileNotFoundError:
#     print("file not found")

# try:
#     with open('test.txt','a') as file:  #append to file
#         file.write(moreText)
# except FileNotFoundError:
#     print("file not found")

### Copying files
# import shutil

# # copyfile() - copies contents of a file
# # copy() - copyfile() + permission mode + destination can be a dir
# # copy2() - copy() + copies metadata (file creation and modification times)

# shutil.copyfile('test.txt','newtest.txt') # src, des
#                                           # copyfile will create the des file

### Moving files (or directories)
# import os

# source = "newtest.txt"
# destination = "C:\\Users\\lwhit\\OneDrive\\newnewtest.txt"  #can rename the file

# try:
#     if os.path.exists(destination):
#         print("there is already a file there")
#     else:
#         os.replace(source,destination)
#         print(source+" was moved")
# except FileNotFoundError:
#     print(source+" was not found")

### Deleting files
# import os, shutil

# path = "test.txt"
# try:
#     os.remove(path) # delete a file
#     # os.rmdir(path)  # delete an empty dir
#     # shutil.rmtree(path) # delete a folder and all files within. DANGEROUS
# except FileNotFoundError:
#     print("file was not found")

################### Modules
# Module = file containing python code. May contain functions, classes, etc.
# used with modular programming / used to separate a program into parts

# import messages as m 
# # from messages import hello, yourname
# # help("modules")

# m.hello()
# m.yourName("Logan")

################### 

