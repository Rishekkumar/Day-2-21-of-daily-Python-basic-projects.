import random
options= ["rock", "paper", "scissors","q"]

user_wins=0
bot_win=0
while True:
    user_input= input("enter your move, rock, paper, or scissors, and q to quit: ").lower()
    rand= random.randint(0,2)
    if user_input not in options:
        print("please input valid move")
        continue
    if user_input== "q":
        print("quit")
        break
    
    bot_move= options[rand]
    print(f"computer choose {bot_move}")
    # print(rand)#delete
    if user_input== "rock"    and bot_move == "scissors":
        print("you won!")
        user_wins += 1
    elif user_input == "paper" and bot_move == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and bot_move == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("you lose ")
        bot_win+=1
print(f"you won {user_wins} times and computer wins{bot_win} times")