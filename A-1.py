class IOstring:
    def __intit__(self):
        self.str1 = ""
    def get_string(self):
        self.str1 = input("Enter a word or string to make it in uppercase letters: ")
    def print_string(self):
        print("Result is: ", self.str1.upper())
str1 = IOstring()

str1.get_string()
str1.print_string()