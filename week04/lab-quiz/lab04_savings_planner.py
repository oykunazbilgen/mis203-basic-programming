def main():
  # 1. Starting balance validation (Cannot be negative)
  while True:
    try:
      starting_balance = float(input("Enter starting balance: "))
      if starting_balance < 0:
        print("Error: Starting balance cannot be negative. Try again.")
        continue
      break
    except ValueError:
      print("Invalid input. Please enter a valid number.")

  # 2. Monthly deposit validation (Must be positive > 0)
  while True:
    try:
      deposit = float(input("Enter monthly deposit: "))
      if deposit <= 0:
        print("Error: Monthly deposit must be positive. Try again.")
        continue
      break
    except ValueError:
      print("Invalid input. Please enter a valid number.")

  # 3. Interest rate validation (Cannot be negative)
  while True:
    try:
      rate = float(input("Enter monthly interest rate (%): "))
      if rate < 0:
        print("Error: Interest rate cannot be negative. Try again.")
        continue
      break
    except ValueError:
      print("Invalid input. Please enter a valid number.")

  # 4. Savings goal validation (Must be positive > 0)
  while True:
    try:
      goal = float(input("Enter savings goal: "))
      if goal <= 0:
        print("Error: Savings goal must be positive. Try again.")
        continue
      break
    except ValueError:
      print("Invalid input. Please enter a valid number.")

  balance = starting_balance
  total_interest = 0.0
  months = 0

  # If the starting balance already meets or exceeds the goal
  if balance >= goal:
    print(
        "\nStarting balance already meets or exceeds the goal! No simulation"
        " needed."
    )
    print(f"Final Balance: ${balance:.2f}")
    print("Total Interest Earned: $0.00")
    return

  # Table header
  print(f"\n{'Month':<6} | {'Interest':<10} | {'Balance':<10}")
  print("-" * 32)

  # Monthly loop (Up to 60 months max)
  for month in range(1, 61):
    interest = balance * (rate / 100.0)
    total_interest += interest
    balance += interest
    balance += deposit
    months = month

    print(f"{month:<6} | {interest:<10.2f} | {balance:<10.2f}")

    # Break out of loop early if goal is reached
    if balance >= goal:
      break

  # Print final results
  print("-" * 32)
  if balance >= goal:
    print(f"Goal reached in {months} months!")
  else:
    print("Goal not reached after 60 months.")

  print(f"Final Balance: ${balance:.2f}")
  print(f"Total Interest Earned: ${total_interest:.2f}")


if __name__ == "__main__":
  main()