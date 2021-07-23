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