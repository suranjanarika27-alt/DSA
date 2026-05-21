def checkValid(nums):
    if len(nums) != 16 and len(nums) != 19:
        print("Invalid")
        return
    num_list = []
    for x in nums:
        if x == " ":
            continue
        elif not x.isdigit():
            print("Invalid")
            return
        else:
            num_list.append(int(x))
    for x in num_list[::2]:
        x *= 2
        if x > 9:
            x -= 9
    if sum(num_list) % 10 == 0:
        print("Valid")
    else:
        print("Invalid")
        
if __name__ == "__main__":
    card_number = input("Enter the credit card number: ")
    checkValid(card_number)