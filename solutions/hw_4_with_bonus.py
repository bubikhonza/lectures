ticket_price = 45
while True:
    age_input = input("Enter your age: ")

    if age_input.isnumeric():
        # Overeni zda je vek kladny lze i v samotne podmince vyse pridanim and int(age_input) > 0 protoze python kontroluje podminku z leva do prava.
        if int(age_input) > 0:
            break
    print(f"Incorrect input! Whole positive number expected, entered: {age_input}")

while True:
    employee_input = input("Are you employee? Y/N: ").lower()
    if employee_input in ["y", "n"]:
        break
    print(f"Incorrect input! Y or N expected, entered: {employee_input}")

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
        print(f"Price: {ticket_price * 0.2}")
    else:
        print(f"Price: {ticket_price}")