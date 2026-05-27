def reverse_string(word):
    reverse = ""
    for i in range(len(word)-1, -1, -1):
        char = word[i]
        reverse = reverse + char
    return reverse

if __name__ == "__main__":
    word = input("Enter a word: ")
    if word == reverse_string(word):
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is not a palindrome.")