y = "patil"

def myFun():
    x = "Chetanya"
    print(x)
    print(y)

# print(x)
myFun()
# print(x)

# If we create a variable with same name inside function, still both local and Global variables are different. 
# Local variables can be used only with in the function.

a = "patil"

def MyFunction():
    a = "chetanya"
    print(a)

MyFunction()
print(a)

# outside the function value of a will be patil and inside the function value will be chetanya.


# Global Keyword

p = "patil"

def MyFunc():
    global p
    p = "Chetanya"
    print(p)

MyFunc()
print(p)



def MyFunc1():
    global r
    r = "Chetanya"

MyFunc()
print(r)