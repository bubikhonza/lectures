ticket_price = 45
age_input = input("Enter your age: ")

if not age_input.isnumeric():
    print(f"Incorrect input! Whole number expected, entered: {age_input}")
    quit()

employee_input = input("Are you employee? Y/N: ").lower()
if employee_input not in ["y", "n"]:
    print(f"Incorrect input! Y or N expected, entered: {employee_input}")
    quit()

age = int(age_input)
is_employee = employee_input == "y"

if age <= 12:
    print("Price: 0")
elif is_employee:
    if age > 55:
        print("Price: 0")
    else:
        print(f"Price: {ticket_price * 0.2}")
else:
    if age < 18:
        print(f"Price: {ticket_price * 0.5}")
    elif age > 65:
        print(f"Price: {ticket_price * 0.7}")
    else:
        print(f"Price: {ticket_price}")
