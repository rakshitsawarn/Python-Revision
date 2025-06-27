# Tell a person if he can vote or not based on his age

age = 8

match age:
    case 9:
        print("Bhai Ghar Baitho, Vote nahi de sakte")
    case 18:
        print("Bhai Vote de sakte ho, jao vote do")
    case _ if age >= 18:
        print("Bhai Vote de sakte ho, jao Bhag k vote do")
    case _ if age < 18:
        print("Bhai Ghar Baitho, Vote nahi de sakte diye to maarenge")



