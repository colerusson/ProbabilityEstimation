import random
import matplotlib.pyplot as plt


def main(games):
    doors = [1, 2, 3]
    staying_wins = 0
    switching_wins = 0

    for i in range(games):
        car = random.choice(doors)
        choice = random.choice(doors)
        if choice == car:
            staying_wins += 1
        else:
            switching_wins += 1

    staying_wins = staying_wins / games
    switching_wins = switching_wins / games

    return staying_wins, switching_wins


if __name__ == "__main__":
    n_values = [10, 100, 1000, 10000, 100000, 1000000]
    staying_wins_data = []
    switching_wins_data = []

    for n in n_values:
        staying_win, switching_win = main(n)
        staying_wins_data.append(staying_win)
        switching_wins_data.append(switching_win)
        print("n = " + str(n) + ": Staying Wins = " + str(staying_win) + ", Switching Wins = " + str(switching_win))

    plt.figure(figsize=(12, 5))

    # Staying Wins
    plt.subplot(1, 2, 1)
    plt.plot(n_values, staying_wins_data, marker='o', linestyle='-')
    plt.xscale('log')  # Use a logarithmic scale on the x-axis
    plt.xlabel('n')
    plt.ylabel('Staying Wins')
    plt.title('Staying Wins vs. n')

    # Switching Wins
    plt.subplot(1, 2, 2)
    plt.plot(n_values, switching_wins_data, marker='o', linestyle='-')
    plt.xscale('log')
    plt.xlabel('n')
    plt.ylabel('Switching Wins')
    plt.title('Switching Wins vs. n')

    plt.tight_layout()
    plt.show()
