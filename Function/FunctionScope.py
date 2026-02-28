# Scope refers to the area of a program where a variable can be accessed or used.

# Types of Scope in Python (LEGB Rule)
# LEGB = Local → Enclosing → Global → Built-in

#  L — Local Scope

def show():
    x = 10
    print(x)
# print(x)   # --- wrong 

# Variables defined inside a function
# Accessible only within that function

# E — Enclosing Scope

def outer():
    x = 10
    def inner():
        print(x)
    inner()   # yes need to call inner function as well to run inner func when outer func get called
outer()       # outter func called 

# Variables in the outer function of a nested function

# Accessible inside inner functions


# G — Global Scope

x = 10
def display():
  global x # if only read then on need global keyword
  x = x + 1
  print(x)
display()

# only read
y = 30   # global variable

def display():
    print(y)

display()


# Variables defined outside all functions

# Accessible throughout the program



# B — Built-in Scope 

# Predefined names in Python

print(len("Python"))


# print(len("Python"))