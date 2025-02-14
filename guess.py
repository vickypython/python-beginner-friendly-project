import random

def check_guess():
    num_rand=random.randint(1,100)
    attempts=0
    
    while True:

        guess=int(input('input your guess num >'))
        attempts=attempts+1
        if guess<num_rand:
            print("Number too low")
        elif guess>num_rand:
            print("Number too high")
        else:
            print(f"You goyt the right num is {guess} with {attempts} attempts")
            break

check_guess()
