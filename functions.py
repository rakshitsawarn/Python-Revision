# Write a function that takes two numbers as input and returns their average.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
def find_average(number1, number2):
    a = number1 + number2
    average = a/2
    print("The average of", number1, "and", number2, "is", average)

find_average(number1, number2)



# Write a function that checks if a number is greater or smaller

def compare_numbers(number1, number2):
    if number1 > number2:
        print("The Number1 is greater than Number2")
    elif number1 == number2:
        print("The Number1 is equal to Number2")
    else:
        print("The Number1 is smaller than Number2")
compare_numbers(number1,number2) 