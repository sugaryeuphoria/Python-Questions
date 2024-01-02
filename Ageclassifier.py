# Taking the user input
person_age = int(input("Enter the age of the person: "))

# declaring conditions
if (person_age<=1):
    print("The person is an infant.")
elif (person_age > 1 and person_age < 13):
    print("The person is a child.")
elif(person_age >= 13 and person_age<20):
    print("The person is a teenager")
else:
    print("The person is an adult.")            


