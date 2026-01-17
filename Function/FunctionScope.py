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
    inner()    
outer()        