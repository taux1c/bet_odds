from random import choice

max_runs = 500
event_round = 0
wins = 0
losses = 0
# This is the percent chance of winning
desired_percentage = 40

def bet_run(bet):
    global wins, losses, event_round, max_runs, desired_percentage
    if event_round == max_runs:
        print("You have reached the maximum amount of rounds, you won {} times and lost {} times".format(wins, losses))
        return
    event_round += 1
    random_number = choice([x for x in range(1, 100)])
    if random_number <= desired_percentage:
        bet_win(bet)
        wins += 1
        bet_run(bet)
    else:
        bet_loss(bet)
        losses += 1
        bet_run(bet)

def bet_loss(bet):
    print("You lost the bet, you lost {} tokens".format(bet))

def bet_win(bet):
    print("You won the bet, you won {} tokens".format(bet))

def main(bet=0):
    if bet == 0:
        bet = int(input("How much do you want to bet? "))
    bet_run(bet)

if __name__ == "__main__":
    main()