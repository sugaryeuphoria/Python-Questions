# Defining a function
def pyramid_pattern(n):
  # Looping over rows of the pyramid
  for i in range(1, n+1):
    # Adding spaces to the left of the pyramid
    for j in range(n-i):
      print(" ",end=" ")
    #Adding stars in the pyramid 
    for k in range(2 * i - 1):
      print("*", end=" ")
    print()

# Taking the user input
n = int(input("Enter the number of rows (within range 1 to 20): "))

# Creating a default error message 
if n < 1 or n > 20:
  print("Please enter a positive integer between 1 and 20")
  n = int(input("Enter the number of rows (within range 1 to 20): "))
  pyramid_pattern(n)
else:
  pyramid_pattern(n)

