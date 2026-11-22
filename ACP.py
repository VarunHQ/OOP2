class DailyMessage:
    def __init__(self):
        self.message = ""

    def get_Message(self):
        self.message = input("Enter the message for today: ")

    def printMessage(self):
        print("Message in Uppercase: ", self.message.upper())

daily_text =  DailyMessage()
daily_text.get_Message()
daily_text.printMessage()

class HelperSession:
    def __init__ (self):
        print("Daily data helper session has been created.")
    def __del__(self):
        print("Daily data helper has been ended.")

def createSession():
    print("Making helper session..")
    session = HelperSession()
    print("Session is ready..")
    return session

print("")
print("Calling create_session() function..")
session_obj = createSession()
print("Program still running..")

class PairFinder:
    def find_pair(self, numbers, target):
        lookup = {}
        for index, number in enumerate(numbers):
            needed_number = target - number 
            if needed_number in lookup:
                return (lookup[needed_number], index)
            lookup[number] = index

        return None

numbers = {10, 20, 30, 40, 50, 60, 70, 80, 90}
target_value = int(input("Enter target sum to search: "))
result = PairFinder().find_pair(numbers, target_value) 

if result is not None:
    print("index1=%d, index2=%d" % result)
else:
    print("No matching pair found. Use another number.")

del session_obj
print("Program End. Thank you for using this program.")