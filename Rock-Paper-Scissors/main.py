import random

choices = ['R', 'P', 'S']



while True:

    cpu = random.choice(choices)

    if cpu == 'R':
        cpu = 'Rock'
    elif cpu == 'P':
        cpu = 'Paper'
    elif cpu == 'S':
        cpu = 'Scissors'
        
    
    choice = input('Pick a choice between "R" for Rock, "P" for Paper or "S"  for Scissor : ')
    choice = choice.upper()
    # loop until valid input is entered
    if choice not in choices:
        print('Invalid input')
        continue		
    else: 
        
        if choice  == 'R':
            choice  = 'Rock'
        elif choice == 'P':
            choice = 'Paper'
        else:
            choice = 'Scissors'

        # printing 
        print(f"Player({choice}) : CPU ({cpu})")

        if cpu == choice:
            print(f"it's a tie. Repeat")
            continue
        else:
            if choice == 'Rock' and cpu == 'Scissors':
                print(f'Player wins. Game over')
                break
            elif choice == 'Paper' and cpu == 'Rock':
                print(f'Player wins. Game over')
                break
            elif choice == 'Scissors' and cpu == 'Paper':
                print(f'Player wins. Game over')
                break
            else:
                print(f'CPU wins. Game over')
                break

            
           