def fibonacci(n, arr):
    if n == 0:
        arr.append(0)
    elif n == 1:
        arr.append(0)
        arr.append(1)
    else:
        fibonacci(n - 1, arr)
        arr.append(arr[-1] + arr[-2])

if __name__ == "__main__":
    terms = int(input("Enter the number of terms: "))
    arr = []
    fibonacci(terms, arr)
    print(arr)