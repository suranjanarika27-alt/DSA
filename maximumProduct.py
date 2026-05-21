def maximumProduct(arr):
    pos , neg = [], [] 
    for x in arr:
        if x > 1 :
            pos.append(x)
        elif x < 0 :
            neg.append(x)
    product = 1
    for x in pos:
        product *= x
    neg.sort()
    if len(neg) % 2 == 0:
        for x in neg:
            product *= x
    else:
        for x in neg[:-1]:
            product *= x
    print(product)

if __name__ == "__main__":
    arr = list(map(int, input("Enter the array:").split()))
    maximumProduct(arr)