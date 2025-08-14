def is_prime(num):
    if num <=1:
        print("It is not a prime number")
        return
    if num == 2:
        print("It is a prime number")
        return
    if num % 2 == 0:
        print("It is not a prime number")
        return
    for i in range(3,int(num ** 0.5) + 1, 2):
        if num % i == 0:
            print("It is not a prime number")
            return
    print("It is a prime number")
    return

print(is_prime(9))  # Example usage