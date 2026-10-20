# Palindrome Checker using Recursion

def is_palindrome(word):

    # Base Case 1
    if len(word) <= 1:
        return True
    # Base Case 2
    if word[0] != word[-1]:
        return False

    # Recursive Step
    return is_palindrome(word[1:-1])


# Testing the function
print("hello:", is_palindrome("hello"))
print("level:", is_palindrome("level"))

# Letting the user enter their own word
word = input("Enter a word: ").lower()

if is_palindrome(word):
    print("This word is a palindrome!")
else:
    print("This word is not a palindrome!")