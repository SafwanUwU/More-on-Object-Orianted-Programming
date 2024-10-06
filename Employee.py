class Employee:

    def __init__(self):
        print("Employee Craeted")

    def __del__(self):
        print("Destructor Called")

def Create_obj():
    print("Starting Function...")
    obj = Employee()
    print("Dunction End...")
    return obj
obj = Create_obj()
print("Program End..")