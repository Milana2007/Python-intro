'''
if (3 > 2 ):
    print ("3 is more than 2")
else:
    print ("3 is not more than 2")
if (3 < 3):
    print ("option 2")
letter = "z"
if (letter == "a"):
    print ("got b")
else:
    print ("got something else")

def print_stuff ():
     print("a function is printing this")
     print ("isn't that cool?!")

print_stuff()

'''
def operation (a, b, c):
    return a**2 + b/4 - cool

#print (operation (3,4,2))
def hello (n):
    return  n*"hello"
print (hello(100))
    # this function not return anyhting
    # this function has a return
    
def rectangle_perimeter(w, h):
    return h+h+w+w 

print (rectangle_perimeter(4, 4))

def rectangle_area(w, h):
    return h+h+w+w

print (rectangle_area(2, 2))

def rectangle_info (w, h, x):
    if x == "a":
        return rectangle_area(width, height)
    elif x =="p":
        return rectangle_perimeter(width, height)
    else:
        return -1
print (rectangle_info (35,1000))
                