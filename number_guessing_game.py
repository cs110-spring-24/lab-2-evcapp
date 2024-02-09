import random

while True:
    num = random.randint(1, 100)
    guess_count = 0
    lower_bound = 1
    upper_bound = 100
    
    while True:
        print(f"Guess a number between {lower_bound} and {upper_bound}:")
        user = int(input())
        guess_count += 1
        
        if user > num:
            print("Too high!")
            upper_bound = user
        elif user < num:
            print("Too low!")
            lower_bound = user
        else:
            print("You win!")
            break
    
    print("It took you", guess_count, "guesses to solve it!")
    
    replay = input("Do you want to play again? (yes/no): ")
    if replay.lower() != 'yes':
        print("Goodbye!")
        break
 

