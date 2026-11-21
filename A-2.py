class Employee:
    def __init__(self):
        print("Employee has been created")

    def __del__(self):
        print("Employee has been destructed")

def CreateObject():
    print("Making object...") 
    obj = Employee()

    print("Function finish...")
    return obj

print("Calling the CreateObject() function...")
obj = CreateObject()
print("Program end thank you...")