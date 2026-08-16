# Build a number guessing game — computer picks a random number, user keeps guessing until correct.
# Guess: 50 → Too low! Guess: 75 → Too high! Guess: 63 → 🎉 Correct!


import random
comp=random.randint(1,100)
tries=0

while True:
    tries=tries+1
    human=int(input("Guess your number between 1-100:- "))
    if human==comp:
        print(f"Congratulations you have won in {tries} tries!!")
        break
    elif human>comp:
        print("Sorry go lower")
    elif human<comp:
        print("Sorry go higher")
