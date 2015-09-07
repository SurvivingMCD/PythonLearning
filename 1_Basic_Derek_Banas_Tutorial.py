# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 15:39:32 2015

@author: Stephane
"""
#Import specialties functions
import random#random number generation
import sys#
import os#operating system

def hello():
    print ("Hello World")
    
hello()
''' 
Multiline comment
'''
name = "Stephane"
print (name)

#Numbers Strings Lists Tuples Dictionaries

#+ - * / % ** exponential // discard the ratio

print(5**2)
print(5/2)
print(5//2)#Only the integer part of the operation


#Tuples () and Lists []
pi_tuple = (3,1,3,2,4)
pi_tuple

new_tuple = list(pi_tuple)
new_tuple

new_list = tuple(new_tuple)
new_list

len(new_list)
len(new_tuple)

max(new_tuple)
min(new_tuple)

a =[1,2,3]
b = [4,5,6]
c = a + b #Concatenate a list 
c

#Dictionaries are similar to hash tables or maps, values with a unique key you can't join dictionaries
personas = {'javier' : '554234',
            'lalo' : '543456',
            'stephane' : '5541393819'}
            
print(personas['stephane'])

del personas['javier']

personas['stephane'] = 'otracosa'

print(len(personas))

print(personas.get('stephane'))

print(personas.keys())#get a list of keys

print(personas.values())#get a list of values

#if else elif
#== != >= <=

age = 21

if age > 16:
    print('You can drive')
else:
    print('You are not old enough to drive')
    
if age >= 21:
    print("You can drive a trailer")
elif age >= 16:
    print("You can drive a car")
else:
    print("You can't drive anything")
    
if (age >= 1 and age <= 18):
    print("You are yyoung")
elif (age != 21 or age >= 65):
    print("Yoiu are old")
elif not(age == 30):
    print("You don't get a birthday")
    
    
#looping
for x in range(0,10,1):#Does not include the last element
    print(x, ' ', end="")
    
print('\n')

grocery_list = ["Juice","Tomatoes","Eggs"]
for y in grocery_list:
    print(y)
for x in [2,4,6,8]:
    print(x)
    
num_list = [[1,2,3],[10,11,12],[23,22]] 
num_list   

num_list[2]
num_list[0][1]

for t in range(len(num_list)):
    print("new item")
    for l in range(len(num_list[t])):
        print(num_list[t][l])
        
help(random.randrange)
random_num = random.randrange(0,100)
random_num
count = 0
while(random_num != 15):
    print(random_num)
    count = count +1
    random_num =random.randrange(0,100)
print("it took ",count,"cycles to get a 15")

i = 0
while (i<=20):
    if(i%2 == 0):
        print(i)
    elif(i==9):
        break
    else:
        i += 1#short hand notation
        continue#skipo rest and jump back in the loop
    i+=1
    
def addNumber(fNum, lNum):
    sumNum= sum(range(fNum,lNum+1))
    return sumNum
    
print(addNumber(1,4))

print("What is your name?")
name = sys.stdin.readline()#No sirve en IPython
print("Your answer was: ",name)

long_string = "           I´ll catch you when you fall - The floor"


print(long_string[0:4])
print(long_string[-5:])#last 5 characters

print(long_string[:10])

print(long_string[10:])
print(long_string[:-5])

print(long_string[:])

print(long_string[0:4]+long_string[10:14])

a = range(10)

a[0:3]

print("%c is my %s letter and my number is %d float is %.5f" % ('X','favorite',1,1.4))

print(long_string.capitalize())

print(long_string.find("floor"))

print(long_string.isalpha())#are all letters

print(long_string.isalnum())#are all numbers

print(len(long_string))

print(long_string.replace("floor","ground"))

print(long_string.strip())

print(long_string.split(" "))

my_parsed_string = long_string.split(" ")
for i in my_parsed_string:
    if(i.isalpha()):
        print("%s is a word" % (i))
    
help(open)
test_file = open("test.txt","wb")


print(test_file.name)
print(test_file.mode)

test_file.write(bytes("La vida es un carnaval"))
test_file.close()

test_file = open("test.txt","r+")
the_text = test_file.read()
print(the_text)
os.remove("test.txt")



class Animal(object):
    __name = ""
    __height = 0
    __weight = 0
    __sound = ""
    
    def __init__(self,name,height,weight,sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound
    
    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name
        
    def get_height(self):
        return self.__height
        
    def get_weight(self):
        return self.__weight
        
    def get_sound(self):
        return self.__sound
        
    def get_type(self):
        print("Animal") 
        
    def toString(self):
        print("{} is {} cm tall and {} kg and makes {}".format(self.__name,self.__height,self.__weight,self.__sound))
        
cat = Animal("Whiskers",33,10,"Meow")
type(cat)
print(cat.toString())        
cat.get_type()
os.chdir("C:\\Users\\Stephane\\Desktop\\ITAM\\Python\\")
os.getcwd()

class Dog(Animal):
    __owner = ""
    
    def __init__(self,name,height,weight,sound,owner):
        self.__owner = owner
        super(Dog,self).__init__(name,height,weight,sound)
        
    def get_owner(self):
        return self.__owner
        
    def get_type(self):
        print("Dog")
        
    def toString(self):
        print("{} is {} cm tall and {} kg he belongs to {} and makes {}".format(self.get_name(),self.get_height(),self.get_weight(),self.__owner,self.get_sound()))
##Method overloading
    def multiple_sounds(self,how_many = None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound()*how_many)
            
spot = Dog("Spot",53,27,"Ruff","Derek")
spot.get_weight()

print(spot.toString())

class AnimalTesting:
    def get_type(self,animal):
        animal.get_type()

test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(spot)

spot.multiple_sounds(4)
spot.multiple_sounds()            

    





a = (1,2,3)
type(a)

