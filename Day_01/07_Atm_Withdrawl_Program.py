# Requirements:
# Ask the user for their account balance.
# Ask how much they want to withdraw.
# If withdrawal amount is greater than balance → "Insufficient balance"
# If withdrawal amount is <= 0 → "Invalid amount"
# Otherwise → deduct the amount and display the remaining balance.

balance = int(input("Enter your accout balance:"))

withdrawl= int(input("Enter amount to withdrawl:"))

if withdrawl > balance:
    print("Insufficient balance")

elif withdrawl <=0:
    print("Invalid amount")

else :
    print(f"You have {withdrawl} succesfully, Remaining balnce is {balance-withdrawl}")