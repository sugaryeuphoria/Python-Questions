
employee_1_id = employee_2_id = 0
employee_1_name = employee_2_name = ""
employee_1_rate = employee_2_rate = 0.0
employee_1_hours = employee_2_hours = 0.0


def add_employee():
    global employee_1_id, employee_1_name, employee_1_rate, employee_1_hours
    global employee_2_id, employee_2_name, employee_2_rate, employee_2_hours

    if employee_1_id == 0:
        employee_1_id = int(input("Enter Employee1 ID: "))
        employee_1_name = input("Enter Employee Name: ")
        employee_1_rate = float(input("Enter Hourly Rate: "))
        employee_1_hours = float(input("Enter Hours Worked: "))
    elif employee_2_id == 0:
        employee_2_id = int(input("Enter Employee2 ID: "))
        employee_2_name = input("Enter Employee Name: ")
        employee_2_rate = float(input("Enter Hourly Rate: "))
        employee_2_hours = float(input("Enter Hours Worked: "))
    else:
        print("Maximum employee limit reached.")

def view_employees():
    if employee_1_id != 0:
        print(f"Employee ID: {employee_1_id}, Name: {employee_1_name}, Hourly Rate: {employee_1_rate}, Hours Worked: {employee_1_hours}")
    if employee_2_id != 0:
        print(f"Employee ID: {employee_2_id}, Name: {employee_2_name}, Hourly Rate: {employee_2_rate}, Hours Worked: {employee_2_hours}")
    if employee_1_id == 0 and employee_2_id == 0:
        print("No employees added yet.")


def calculate_payroll():
    if employee_1_id != 0:
        tax_rate = float(input("Enter Tax Rate (in %): "))
        benefit_amount = float(input("Enter Benefit Amount: "))

        gross_salary_1 = employee_1_rate * employee_1_hours
        tax_deduction_1 = (gross_salary_1 * tax_rate) / 100
        net_salary_1 = gross_salary_1 - tax_deduction_1 + benefit_amount

        print(f"Employee ID: {employee_1_id}, Name: {employee_1_name}, Gross Salary: {gross_salary_1}, Tax Deduction: {tax_deduction_1}, Benefit Amount: {benefit_amount}, Net Salary: {net_salary_1}")

    if employee_2_id != 0:
        tax_rate = float(input("Enter Tax Rate (in %): "))
        benefit_amount = float(input("Enter Benefit Amount: "))

        gross_salary_2 = employee_2_rate * employee_2_hours
        tax_deduction_2 = (gross_salary_2 * tax_rate) / 100
        net_salary_2 = gross_salary_2 - tax_deduction_2 + benefit_amount

        print(f"Employee ID: {employee_2_id}, Name: {employee_2_name}, Gross Salary: {gross_salary_2}, Tax Deduction: {tax_deduction_2}, Benefit Amount: {benefit_amount}, Net Salary: {net_salary_2}")

    if employee_1_id == 0 and employee_2_id == 0:
        print("No employees added yet.")

# Function to delete an employee
def delete_employee():
    employee_id = int(input("Enter Employee ID to delete: "))
    
    global employee_1_id, employee_2_id, employee_1_name, employee_2_name
    global employee_1_rate, employee_2_rate, employee_1_hours, employee_2_hours
    
    if employee_id == employee_1_id:
        employee_1_id, employee_1_name, employee_1_rate, employee_1_hours = 0, "", 0.0, 0.0
    elif employee_id == employee_2_id:
        employee_2_id, employee_2_name, employee_2_rate, employee_2_hours = 0, "", 0.0, 0.0
    else:
        print("Employee not found.")



def adjust_salary():
    employee_id = int(input("Enter Employee ID to adjust salary: "))
    new_hourly_rate = float(input("Enter New Hourly Rate: "))

    if employee_id == employee_1_id:
        employee_1_rate = new_hourly_rate
    elif employee_id == employee_2_id:
        employee_2_rate = new_hourly_rate
    else:
        print("Employee not found.")

def search_employee():
    search_name = input("Enter Employee Name to search: ")

    if search_name.lower() == employee_1_name.lower():
        print(f"Employee ID: {employee_1_id}, Name: {employee_1_name}, Hourly Rate: {employee_1_rate}, Hours Worked: {employee_1_hours}")
    if search_name.lower() == employee_2_name.lower():
        print(f"Employee ID: {employee_2_id}, Name: {employee_2_name}, Hourly Rate: {employee_2_rate}, Hours Worked: {employee_2_hours}")


def main():
    while True:
        print("\nMain Menu:")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Calculate Payroll")
        print("4. Delete Employee")
        print("5. Adjust Salary")
        print("6. Search Employee")
        print("7. Quit")

        choice = int(input("Enter your choices 1/2/3/4/5/6/7: "))

        if choice == 1:
            add_employee()
        elif choice == 2:
            view_employees()
        elif choice == 3:
            calculate_payroll()
        elif choice == 4:
            delete_employee()
        elif choice == 5:
            adjust_salary()
        elif choice == 6:
            search_employee()
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please try again.")


main()
