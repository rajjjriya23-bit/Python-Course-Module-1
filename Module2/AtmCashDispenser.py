# ATM Cash Dispenser

print("=== ATM Cash Dispenser ===")
print("Dispensing cash for customers one at a time.\n")

notes = [100, 50, 20, 10, 5, 1]
customers_served = 0
total_dispensed = 0
log = []   # stores each customer's note breakdown for the daily report

# Outer while loop — runs once per customer
serving = True
while serving:

    name = input("Enter customer name: ")
    amount = int(input(f"Hello {name}! Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount. Please enter a positive number.\n")
        continue

    print(f"\nDispensing {amount} units for {name}:")
    print("-" * 30)

    remaining = amount
    i = 0
    used = {}

    # Inner while loop — breaks amount into notes
    while i < len(notes):
        count = remaining // notes[i]
        if count > 0:
            print(f"  {count}  x  {notes[i]}-unit note(s)  =  {count * notes[i]}")
            used[notes[i]] = count
            remaining -= count * notes[i]
        i += 1

    customers_served += 1
    total_dispensed += amount
    log.append({"name": name, "used": used})
    print(f"Transaction complete! Please collect your cash, {name}.\n")

    again = input("Next customer? (yes / no): ").strip().lower()
    if again != "yes":
        serving = False

# Outer for loop — goes through each denomination
print("\n=== Daily Denomination Report ===")
for note in notes:
    total_notes = 0
    # Inner for loop — checks every customer's usage of this denomination
    for entry in log:
        total_notes += entry["used"].get(note, 0)
    if total_notes > 0:
        print(f"  {note}-unit notes dispensed today : {total_notes}")

print(f"\nCustomers served : {customers_served}")
print(f"Total dispensed  : {total_dispensed} units")
print("ATM session closed. Goodbye!")
