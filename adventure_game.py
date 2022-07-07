def home():
    print("your mom ask you to go to the store")
    choice = input("stay home (h) or go to the store (s): ")
    if choice == "s":
        path()
    elif choice =="h":
        print ("you fall asleep")
        home()
    else:
        home()
#def store():
def path():
    print("you go to the store and on your way to the store you cross a small Shed, It smell so bad")
    choice = input ("go in the shed (s) or go to the store (t): ")
    if choice =="s":
        shed()
    elif choice == "t":
        store()
    else:
        path()

def shed():
    print("you go towrads the door and try to pull on it and it's locked")
    choice = input ("break the door (b) or go to the store (t)")

def store():
    return

home()