def findMinimumSwaps(initial, final):
    n = len(initial)
    swaps = 0
    for i in range(n):
        if initial[i] != final[i]:
            wrong_index = initial.index(final[i])
            for j in range(wrong_index, i, -1):
                initial[j], initial[j - 1] = initial[j - 1], initial[j]
                swaps += 1
        if initial == final:
            print(swaps)
            return   
    
# i = 3 4 5 6 7
# wrong_index = 
# initial  = 10 20 50 70 90
# final     = 10 20 50 70 90
# initial.index(50) = 3
if __name__ == "__main__":
    initial = list(map(int, input("Enter the initial array:").split()))
    final = list(map(int, input("Enter the final array:").split()))
    findMinimumSwaps(initial, final)