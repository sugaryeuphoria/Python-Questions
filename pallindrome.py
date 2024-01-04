# def is_palindrome(number):
#     # Convert the number to a string for easier comparison
#     num_str = str(number)
    
#     # Compare the original string with its reverse
#     return num_str == num_str[::-1]

# # Input from the user
# num = int(input("Enter a number: "))

# if is_palindrome(num):
#     print(num, "is a palindrome number.")
# else:
#     print(num, "is not a palindrome number.")

def counter(word):
    word = word.lower()
    vowels = "aeiou"
    v=0
    c=0
    for char in word:
        if char in vowels:
            v += 1
           
        else:
            c = c + 1
          

word = input("Enter a string: ")
counter(v)
