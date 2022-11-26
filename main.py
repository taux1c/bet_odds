from random import choice


house_wins = 0
player_wins = 0
house_earnings = 0
player_earnings = 0
game_round = 0
max_game_rounds = 500
house_bank = 100
player_bank = 100
escrow = 0
winning_percentage = 50

def play(bet):
    global house_bank, player_bank, escrow, house_wins, player_wins, house_earnings, player_earnings, game_round
    if bet == 0:
        bet = int(input("How much would you like to bet? "))
    number = choice(range(0, 100))

    if not checks(bet):
        return
    game_round += 1
    if not take_bet(bet):
        return
    if number <= winning_percentage:
        win()
        play(bet)
    else:
        lose()
        play(bet)

def checks(bet):
    global house_bank, player_bank, escrow
    if bet > player_bank:
        print("You don't have enough money to bet that much.")
        game_over()
        return False
    if bet > house_bank:
        print("The house doesn't have enough money to bet that much.")
        game_over()
        return False
    if game_round > max_game_rounds:
        print("The house has reached the maximum number of rounds.")
        game_over()
        return False
    if not escrow == 0:
        print("The escrow is not empty.")
        game_over()
        return False
    return True

def take_bet(bet):
    global house_bank, player_bank, escrow
    try:
        escrow += (bet * 2)
        player_bank -= bet
        house_bank -= bet
    except:
        print("Error taking bet.")
        return False
    return True


def win():
    global house_bank, player_bank, escrow, house_wins, player_wins, house_earnings, player_earnings
    print("You won.")
    try:
        player_bank += escrow
        player_wins += 1
        player_earnings += escrow/2
        escrow = 0
    except:
        print("Error with winnings.")


def lose():
    global house_bank, player_bank, escrow, house_wins, player_wins, house_earnings, player_earnings
    print("You lost.")
    try:
        house_bank += escrow
        house_wins += 1
        house_earnings += escrow/2
        escrow = 0
    except:
        print("Error with bet.")

def display_stats():
    global house_wins, player_wins, house_earnings, player_earnings
    print("House wins: " + str(house_wins))
    print("Player wins: " + str(player_wins))
    print("House earnings: " + str(house_earnings))
    print("Player earnings: " + str(player_earnings))
    print("You won " + str(round((player_wins / game_round) * 100, 2)) + "% of the time.")
    print("The house bank is " + str(house_bank))
    print("The player bank is " + str(player_bank))
    print("You played " + str(game_round) + " rounds.")

def game_over():
    print("Game over.")
    display_stats()
    exit()

if __name__ == "__main__":
    play(bet=0)
