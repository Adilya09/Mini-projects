import sys
def get_winner(p1, p2):
    if p1 == "q" or p2 == "q":
        sys.exit("Game is over!")
    elif p1 == p2:
        return "It's a tie!"
    elif p1 == "rock":
        if p2 == "scissor":
            return "First player win!"
        else:
            return "Second player win!"
    elif p1 == "paper":
        if p2 == "rock":
            return "First player win!"
        else:
            return "Second player win!"
    elif p1 == "scissor":
        if p2 == "paper":
            return "First player win!"
        else :
            return "Second player win"
    else:
        return "Invalid input!"

print("""Enter your choice in corresponding line.\nIf you want to quit the game enter q.""")


while True:
    player1 = input("First player: rock, paper or scissors: ")
    player2 = input("Second player: rock, paper or scissors: ")
    print(get_winner(player1, player2))



















