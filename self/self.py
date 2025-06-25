a = int(input("Enter Number first: "))
b = int(input("Enter Number second: "))

class Calculator:
    def add(self,a,b):
        return a+b
    def substraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        if b==0:
            print("Error please change the value of b")
        return a/b
    def division_remove_float(self, a,b):
        if b == 0:
            print ("Change the value of b")
        return a//b
    def exponential(self, a, b):
        return a ** b
    
        
d = input("Enter the Desired Operation: ")

if d == "Addition":
    print(a+b)

elif(d == "Substraction"):
    print(a-b)

elif(d == "Multiplication"):
    print(a*b)

elif(d == "Division"):
    print (a/b)
elif(d== "Remove Float"):
    print (a//b)
elif(d == "Exponential"):
    print(a**b)
else:
    print("Kindly choose among Addition \n Substraction \n Multiplication \n Division \n Remove Float \n Exponential")
