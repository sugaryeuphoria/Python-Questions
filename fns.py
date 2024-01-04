# def vowel_count(string):
#     vowel = 0
#     for char in string:
#         if char in "aeiouAEIOU":
#             vowel = vowel + 1
#     return vowel

# def main():
#     user_input=input("Enter a string : ")
    
#     print(vowel_count(user_input))
# main()

# Question2 WAP to find maximum of three numbers
# num1=int(input("Enter number 1: "))
# num2=int(input("Enter number 2: "))
# num3=int(input("Enter number 3: "))

# def max_num(a,b,c):
#     if a > b and b > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c
    
# def main():
#     print(max_num(num1,num2,num3))    
# main()  

# WAP to swap two numbers by passing values
# def swap(a,b):
#     a,b = b,a
#     return a,b

# def main():
#     num1=int(input("Enter number 1: "))
#     num2=int(input("Enter number 2: "))
#     num3, num4 = swap(num1,num2) 
#     print(num3,num4)

# main()

# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
# def factorial(num):
#     fact = 1
#     if num < 0:
#         print("Factorial does not exist for negative numbers")
#     elif num == 0:
#         return 1
#     else:
#         for i in range(1, num+1):
#             fact = fact * i 
#             # fact = 18
#     return fact

# def main():
#     number = int(input("Enter a number: "))
#     print(factorial(number))

# main()   

# randrange
# from random import randrange, randint


# num1 = randrange(1, 5)
# num2 = randint(1, 10)
# print(num1, num2)
