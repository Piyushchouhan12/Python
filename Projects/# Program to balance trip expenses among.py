# Program to balance trip expenses among friends

n = int(input("Enter number of people: "))

people = {}
for i in range(n):
    name = input(f"\nEnter name of person {i+1}: ")
    paid = float(input(f"How much did {name} pay? ₹"))
    people[name] = paid

total = sum(people.values())
equal_share = total / n

print("\n----- Trip Summary -----")
print(f"Total Trip Amount: ₹{total:.2f}")
print(f"Each Person's Share: ₹{equal_share:.2f}\n")

for name, paid in people.items():
    balance = paid - equal_share
    if balance > 0:
        print(f"{name} should get back ₹{balance:.2f}")
    elif balance < 0:
        print(f"{name} should pay ₹{abs(balance):.2f}")
    else:
        print(f"{name} is settled up.")
