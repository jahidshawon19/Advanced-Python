############################# DECORATORS ###################################

""" 
defination: decorators are a way to change or modify 
the behavior of any of your functions or methods 
without directly changing any of the code" 


"""

# prog-1 

# def div(x,y): # div function calculation division for two numbers 
#     if x < y: # issue is here we had to change in our function.
#         x,y = y,x 
#     print(x/y)

# to fix this issue we can apply decorators below 

def div(x,y): # div function calculation division for two numbers 
    print(x/y)

def my_decorator(f):  # here f contains div() function 

    def inner(x,y): # this function performs to swapping variable 
        if x < y:
            x,y = y,x 
            return f(x,y)
    return inner 


if __name__ == "__main__":
    result  = my_decorator(div)
    result(5,15)



############################# GENERATORS ###################################

'''
Generator functions allow you to declare a function that behaves like an iterator.
They allow programmers to make an iterator in a fast, easy, and clean way.
it is Saving memory space.


'''

#prog-1
def sqaure():
    n=1
    while n <= 10:
        sq = n*n;
        yield sq  #Yield is generally used to convert a regular Python function into a generator
        n += 1

result = sqaure()
for i in result:
    print(i)



############################# CONTEXT MANAGER - FILE HANDLING ###################################

'''
context manager allows us to properly manage resources so that we can specify exactly what we want to set up.

'''

with open('employee.txt', 'r') as f:
    print(f.read()) # print whole content 
    print(f.readline()) # print line by line
    print(f.read(10)) #print first 10 char 


############################# MULTITHREADING ###################################

from time import sleep 
from threading import *


class Airstrike(Thread):
    def run(self):
        for i in range(5):
            print("Lunch Bomb")
            sleep(2)


class Artillery(Thread):
    def run(self):
        for i in range(5):
            print("Throw Rocket")
            sleep(2)

captain_tahmid = Airstrike()
colonel_guljar = Artillery()

captain_tahmid.start()
sleep(3)
colonel_guljar.start() 


captain_tahmid.join()
colonel_guljar.join() 


print("Destroyed Israel!")
