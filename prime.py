if __name__ == "__main__":
    num = int(input("Enter a positive number: "))
    if num > 1:
        for i in range(2, num // 2):
            if (num % i) == 0:
                print(f"{num} is not a prime number.")
                break
        else:
            print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")