import random

while True:
    comp=random.randint(1,3)
    human=int(input("Guess rock-1 paper-2 scissors-3:- "))


    if human not in [1,2,3]:
        print("Invalid choice! Choose 1, 2, or 3.")
        continue


    if comp == human:
            print(f"It's a Tie! Both choose {comp}.")
    elif (comp==1 and human==3) or (comp==2 and human==1) or (comp==3 and human==2) :
        print("Computer Won")
    else:
        print("You Won")