
# Question 1

# for i in range (6):
#     print(i)

#Question2 
# num = int(input("Enetr a number: "))

# reverse = 0
# original_num = num
# while num > 0:
#     digit = num % 10
#     reverse =reverse * 10 + digit
#     num = num // 10

# print("Reverse of",original_num," is ", reverse)
# print(reverse.toString())


# Write a program in Python to display the Factorial of anumber.
# num = int(input("Enter a number: "))
# factorial = 1
# if num < 0:
#     print("Factorial is  not defined for negative numbers.")
# elif num == 0:
#     print("1")
# else:
#     for i in range(1,num+1):
#          factorial *= i               
#         #  factorial = factorial * i
#     print(factorial)        

# Write a program to print n natural number in descending order using a while loop
# Input the value of n from the user
# n = int(input("Enter the value of n: "))

# # Initialize the counter to n
# counter = n

# # Use a while loop to print natural numbers in descending order
# while counter >= 1:
#     print(counter, end=" ")
#     counter -= 1


#row = 8
#for i in range(1,row+1):
  #  for j in range(1,i+1):
  #      print(i*j,end=" ")
   # print("")

# row = 5
# for i in range(row,0,-1):
#     for j in range(i,0,-1):
#        print(j,end=" ")
#    print("")

#=========================
# row = 5
# for i in range(1,row+1,1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print("")
