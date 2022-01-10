import random

rounds = int(input("Enter how many rounds you want to play?\n"))

moves = ['rock', 'paper', 'scissors']

p_score = 0
c_score = 0

for i in range(rounds):
    print(f"Round {i + 1}")

    c_index = random.randint(0, 2)
    c_move = moves[c_index]

    p_move = input("Enter your choice: rock,paper,scissors\n").lower()

    if p_move in moves:
        print(f"Player Move {p_move}")
        print(f"Computer Move {c_move}")

        if p_move == "rock" and c_move == "rock":
            winner = "tie"
        elif p_move == "rock" and c_move == "paper":
            winner = "computer"
        elif p_move == "rock" and c_move == "scissors":
            winner = "player"

        elif p_move == "paper" and c_move == "rock":
            winner = "player"
        elif p_move == "paper" and c_move == "paper":
            winner = "tie"
        elif p_move == "paper" and c_move == "scissors":
            winner = "computer"

        elif p_move == "scissors" and c_move == "rock":
            winner = "computer"
        elif p_move == "scissors" and c_move == "paper":
            winner = "player"
        elif p_move == "scissors" and c_move == "scissors":
            winner = "tie"

        if winner == "player":
            p_score += 1
        elif winner == "computer":
            c_score += 1
        else:
            print("It's a tie")

    else:
        print("Inavalid")

if p_score > c_score:
    print(f"Player wins {p_score}")
elif p_score < c_score:
    print(f"Computer wins {c_score}")
else:
    print("Tie tie fish")

