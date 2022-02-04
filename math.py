#add implementation
def add(x,y):
    return x+y
#subtract implementation
def subtract(x,y):
    return x-y    #on master branch
#multiply implementation
def multiply(x,y):
    return x*y #on bug456
#divide implementation
def divide(x,y):  
    if y==0:        #on master branch
       return divide_0_error
    else:
       return x/y

def divide(x,y):  
    return x/y