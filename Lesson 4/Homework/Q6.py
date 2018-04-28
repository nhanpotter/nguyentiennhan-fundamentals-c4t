class String:
    def __init__(self):
        self.string1=""
    def get_String(self):
        self.string1= input("Input string:")
    def print_String(self):
        print(self.string1.upper())
string1=String()
string1.get_String()
string1.print_String()