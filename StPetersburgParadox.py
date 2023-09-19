import random
import matplotlib.pyplot as plt


def main(games):
    coin = ['heads', 'tails']
    average_winnings = 0
    biggest_win_value = 0

    for i in range(games):
        flips = 0
        while True:
            flips += 1
            if random.choice(coin) == 'tails':
                break
        average_winnings += (2 ** flips)
        if 2 ** flips > biggest_win_value:
            biggest_win_value = 2 ** flips

    average_winnings = average_winnings / games
    biggest_win_value = biggest_win_value

    return average_winnings, biggest_win_value


if __name__ == "__main__":
    n_values = [10, 100, 1000, 10000, 100000, 1000000]
    avg_winnings_data = []
    biggest_win_data = []

    for n in n_values:
        avg_winnings, biggest_win = main(n)
        avg_winnings_data.append(avg_winnings)
        biggest_win_data.append(biggest_win)
        print("n = " + str(n) + ": Average Winnings = " + str(avg_winnings) + ", Biggest Win = " + str(biggest_win))

    plt.figure(figsize=(12, 5))

    # Average Winnings
    plt.subplot(1, 2, 1)
    plt.plot(n_values, avg_winnings_data, marker='o', linestyle='-')
    plt.xscale('log')  # Use a logarithmic scale on the x-axis
    plt.xlabel('n')
    plt.ylabel('Average Winnings')
    plt.title('Average Winnings vs. n')

    # Biggest Win
    plt.subplot(1, 2, 2)
    plt.plot(n_values, biggest_win_data, marker='o', linestyle='-')
    plt.xscale('log')
    plt.xlabel('n')
    plt.ylabel('Biggest Win')
    plt.title('Biggest Win vs. n')

    plt.tight_layout()
    plt.show()
