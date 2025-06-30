# 1. Print a square using for and while loop * 
# 1 (a). Print a square using * and for loop

n = 4 
for i in range(n):

    for j in range(n):

        print("*", end = " ")

    print()

print("Square Pattern Problem \n")


# 2 (a). Print a Right Angled Traingle left-alligned using * and for loop


n = 5 
for i in range(1,n):

    print("*" * i)
print("Right Angled Traingle left-alligned Pattern Problem \n")



# 3 (a). Print a Right Angled Traingle right-alligned using * and for loop

n = 6
for i in range(1, n-1):
    print("  " * (n - i) + "* " * i)
print("Right Angled Traingle right-alligned pattern solved \n")



# 4 (a). Print an Inverted Triangle

n = 4 
for i in range(n, 0, -1):
    print("*" * i)
print("Inverted Triangle pattern problem Solved...\n")


# 5 (a). Print a Pyramid Structure using * and for loop...
n = 8
for i in range(n):
    print("  " * (n - i - 1) + "* " * (2 * i + 1))
print("Pyramid pattern Problem Solved.\n")



# 6 (a). Print an Inverted Pyramid
n = 8
for i in range(n, 0, -1):
    print("  " * (n - i - 1) + "* " * (2 * i + 1))
print("Inverted Pyramid Problem Solved")