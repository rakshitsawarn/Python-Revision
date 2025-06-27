class Nested:
    def Negative(self, number):
        if number < 0:
            print("Negative Number")
        elif number == 0:
            print("Nummber is Zero")
            if number > 0:
                print("Number is Positive")
            else:
                print("Enter a Valid Number")

nest = Nested()
nest.Negative(5)

