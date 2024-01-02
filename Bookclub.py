# Take the user input regarding the number of books purchased 
books_purchased = int(input("Enter the number of books purchased this month: "))

# Initial points
points = 0

# Calculating points based on the number of the books purchased
if books_purchased == 0:
    points = 0
elif books_purchased > 0 and books_purchased <= 2:
    points = 5
elif books_purchased > 2 and books_purchased <= 4:
    points = 15        
elif books_purchased > 4 and books_purchased <= 6:
    points = 30
else:
    points = 60

# Printing the number of points awarded
print(f"You have earned {points} points in this month.") 


