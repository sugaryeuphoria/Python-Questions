# character = input("Enter a character from A-Z/a-z: ")
# character = character.lower()

# if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
#     print("The character is a vowel.")

# else:
#     print("The character is not a vowel")    

def isVowel(char):
    char = char.lower()
    if char in ['a','e','i','o','u']:
        return True
    else:
        return False 
user_input = input("Enter a character: ")

if len(user_input) == 1:
    if is_vowel(user_input):
        print(f"{user_input} is a vowel.")
    else:
        print(f"{user_input} is not a vowel.")
else:
    print("Please enter a single character.")
