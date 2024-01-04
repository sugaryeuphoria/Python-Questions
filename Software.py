# Taking the quantity of packages purchased by the user
quantity = int(input("Enter the quantity of packages purchased: "))

# Declaring price per package
price_of_package = 99

# Initial discount and total amount
percentage_of_discount = 0 
total_amount = 0

# Stating the conditions of the discount based on the quantity
if quantity >= 10 and quantity <= 19:
    percentage_of_discount = 10
elif quantity >= 20 and quantity <= 49:
    percentage_of_discount = 20
elif quantity >= 50 and quantity < 99:
    percentage_of_discount = 30        
elif quantity >= 100:
    percentage_of_discount = 40

# Calculating the total amount after adding the discount
amount_of_discount = (percentage_of_discount/100) * (price_of_package * quantity)
total_amount = (price_of_package * quantity) - amount_of_discount

# Printing the discount and total amount of the purchase
print(f"The discount percentage is : {percentage_of_discount}%")
print(f"The discounted amount is ${amount_of_discount}")
print(f"The total amount after discount is : ${total_amount:.2f}")

