# # Using list comprehension to create a list of even numbers from 1 to 100
# my_list = [x for x in range(1, 101) if x % 2 == 0]

# # Print the resulting list
# print(my_list)

# # Q1
# # Create a tuple of numbers from 1 to 10
# numbers_tuple = tuple(range(1, 11))

# # Calculate the sum of all numbers in the tuple
# sum_of_numbers = sum(numbers_tuple)

# # Print the tuple and the sum
# print("Tuple of Numbers:", numbers_tuple)
# print("Sum of Numbers:", sum_of_numbers)

# # del:removes an element from a
# # specific index in a list


# """
# from random import randint
# nums1=tuple(randint(1,100) for x in range(1,10+1)) 
# nums2=tuple(randint(1,100) for x in range(1,10+1)) 
# nums3=tuple(randint(1,100) for x in range(1,10+1)) 
# product = tuple(a*b*c for a,b,c in zip(nums1,nums2,nums3))
# print(product) 
# ya we have done these already in ppt leave it move forward we have a lot ot d0
# str="python"
# reverse = str[::-1]
# print(reverse)

# user_input = input("Enter the String: ")
# ord_nums = [ord(x) for x in user_input]
# characters = [chr(x) for x in ord_nums]
# print("".join(characters))

# dictionary = {}
# dictionary['name']="Pig"
# dictionary['age'] = 35
# dictionary['contact']=364278364
# for key,value in dictionary.items():
#     print(key,value)

# for keys in dictionary.keys():
#     print(keys)
# """

# # Create an empty dictionary to store birthdays
# birthday_dict = {}

# # Step 1: Create a birthday dictionary for 10 persons
# for i in range(10):
#     person_name = input("Enter the person's name: ")
#     person_birthday = input("Enter the person's birthday (MM/DD): ")
#     birthday_dict[person_name] = person_birthday

# # Step 2: Check if a person's birthday exists and update it
# check_name = input("Enter the name to check for birthday: ")
# if check_name in birthday_dict:
#     print(f"{check_name}'s birthday is on {birthday_dict[check_name]}.")
# else:
#     new_birthday = input(f"Enter {check_name}'s birthday (MM/DD): ")
#     birthday_dict[check_name] = new_birthday
#     print(f"{check_name}'s birthday has been updated to {new_birthday}.")

# # Step 3: Remove redundant (duplicate) data
# unique_birthday_dict = {}
# for name, birthday in birthday_dict.items():
#     if birthday not in unique_birthday_dict.values():
#         unique_birthday_dict[name] = birthday

# # Display the updated unique dictionary
# print("Updated Birthday Dictionary:")
# for name, birthday in unique_birthday_dict.items():
#     print(f"{name}'s birthday is on {birthday}.")


# Create two tuples of numbers
tuple1 = (2, 3, 5)
tuple2 = (4, 2, 1)

# Calculate the product of the two tuples
product = tuple1[0] * tuple2[0] + tuple1[1] * tuple2[1] + tuple1[2] * tuple2[2]

# Print the result
print("Product of the two tuples:", product)



# Input: Get a number from the user
number = int(input("Enter a number: "))

# Using list comprehension to create a list of tuples (number and its square)
tuples_list = [(num, num**2) for num in range(1, number + 1)]

# Print the list of tuples
print("List of Tuples (Number, Square):", tuples_list)



# string = "Hello World"
new_string = string.replace("Hello", "Hi")
print(new_string) # Output: Hi World


# Take user values to create a list of strings
user_list = input("Enter a list of strings separated by spaces: ").split()

# Check if "yellow" is in the list
if "yellow" in user_list:
    print("Yes, 'yellow' is in the list.")
else:
    print("No, 'yellow' is not in the list.")

# Check if "orange" is not in the list
if "orange" not in user_list:
    print("Yes, 'orange' is not in the list.")
else:
    print("No, 'orange' is in the list.")
