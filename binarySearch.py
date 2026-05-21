def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2
    while low <= high:
        if arr[mid] == target:
            print(f"Element found at index: {mid}")
            return
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    print("Element not found in the array.")
    return 

if __name__ == "__main__":
    findthis = int(input("Enter the target:"))
    insidethisarray = list(map(int, input("Enter the array:").split()))
    insidethisarray.sort()
    print("Sorted array:", insidethisarray)
    binarySearch(insidethisarray, findthis)



#"1"-->integer-->1
#1 2 3 4 5--> "1 2 3 4 5"--> "1", "2", "3", "4", "5"--> 1, 2, 3, 4, 5 --> [1, 2, 3, 4, 5]
