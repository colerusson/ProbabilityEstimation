import random
import matplotlib.pyplot as plt


def main1(games):
    dice = [1, 2, 3, 4, 5, 6]
    attacker_dice_choices = [3, 3, 2, 2, 1, 1]
    defender_dice_choices = [2, 1, 2, 1, 2, 1]
    game_stats = []

    for i in range(6):
        attacker_army_losses = 0
        defender_army_losses = 0
        for j in range(games):
            attacker = random.choices(dice, k=attacker_dice_choices[i])
            defender = random.choices(dice, k=defender_dice_choices[i])
            attacker.sort(reverse=True)
            defender.sort(reverse=True)
            if attacker[0] > defender[0]:
                defender_army_losses += 1
            else:
                attacker_army_losses += 1

            if attacker_dice_choices[i] > 1 and defender_dice_choices[i] > 1:
                if attacker[1] > defender[1]:
                    defender_army_losses += 1
                else:
                    attacker_army_losses += 1

        results = [attacker_dice_choices[i], defender_dice_choices[i], attacker_army_losses, defender_army_losses]
        game_stats.append(results)

    return game_stats


def main2(games):
    dice = [1, 2, 3, 4, 5, 6]
    game_stats = []

    for i in range(2, 21):
        attacker_win_count = 0
        defender_win_count = 0

        for j in range(games):
            attacker_armies = i
            defender_armies = 5

            while attacker_armies > 1 and defender_armies > 0:
                attacker_dice = 3
                defender_dice = 2
                if attacker_armies == 3:
                    attacker_dice = 2
                elif attacker_armies == 2:
                    attacker_dice = 1

                if defender_armies == 1:
                    defender_dice = 1

                attacker = random.choices(dice, k=attacker_dice)
                defender = random.choices(dice, k=defender_dice)
                attacker.sort(reverse=True)
                defender.sort(reverse=True)

                if attacker[0] > defender[0]:
                    defender_armies -= 1
                else:
                    attacker_armies -= 1

                if attacker_dice > 1 and defender_dice > 1:
                    if attacker[1] > defender[1]:
                        defender_armies -= 1
                    else:
                        attacker_armies -= 1

            if attacker_armies > 1:
                attacker_win_count += 1
            else:
                defender_win_count += 1

        attacker_win_count = attacker_win_count / games
        defender_win_count = defender_win_count / games
        results = [i, attacker_win_count, defender_win_count]
        game_stats.append(results)

    return game_stats


def main3(games):
    dice = [1, 2, 3, 4, 5, 6]
    attacker_armies_left = {}
    defender_armies_left = {}
    for i in range(2, 11):
        attacker_armies_left[i] = 0
    for i in range(1, 11):
        defender_armies_left[i] = 0

    for i in range(games):
        attacker_armies = 10
        defender_armies = 10

        while attacker_armies > 1 and defender_armies > 0:
            attacker_dice = 3
            defender_dice = 2
            if attacker_armies == 3:
                attacker_dice = 2
            elif attacker_armies == 2:
                attacker_dice = 1

            if defender_armies == 1:
                defender_dice = 1

            attacker = random.choices(dice, k=attacker_dice)
            defender = random.choices(dice, k=defender_dice)
            attacker.sort(reverse=True)
            defender.sort(reverse=True)

            if attacker[0] > defender[0]:
                defender_armies -= 1
            else:
                attacker_armies -= 1

            if attacker_dice > 1 and defender_dice > 1:
                if attacker[1] > defender[1]:
                    defender_armies -= 1
                else:
                    attacker_armies -= 1

        if attacker_armies > 1:
            attacker_armies_left[attacker_armies] += 1
        else:
            defender_armies_left[defender_armies] += 1

    for i in range(2, 11):
        attacker_armies_left[i] = attacker_armies_left[i] / games
    for i in range(1, 11):
        defender_armies_left[i] = defender_armies_left[i] / games

    return attacker_armies_left, defender_armies_left


if __name__ == "__main__":
    outcome1 = main1(100000)
    outcome2 = main2(10000)
    attackerOutcome, defenderOutcome = main3(100000)

    plt.figure(1)
    plt.plot(["3:2", "3:1", "2:2", "2:1", "1:2", "1:1"], [outcome1[i][2] for i in range(6)], label="Attacker")
    plt.plot(["3:2", "3:1", "2:2", "2:1", "1:2", "1:1"], [outcome1[i][3] for i in range(6)], label="Defender")
    plt.xlabel("Combination of Attacker to Defender Dice")
    plt.ylabel("Number of Armies Lost - 100,000 Games")
    plt.title("Different Number of Dice")
    plt.legend()
    plt.show()

    plt.figure(2)
    plt.plot([outcome2[i][0] for i in range(19)], [outcome2[i][1] for i in range(19)], label="Attacker")
    plt.plot([outcome2[i][0] for i in range(19)], [outcome2[i][2] for i in range(19)], label="Defender")
    plt.xlabel("Number of Attacker Armies")
    plt.ylabel("Probability of Winning Territory")
    plt.title("Attacker Advantage")
    plt.legend()
    plt.show()

    plt.figure(3)
    plt.plot([i for i in range(2, 11)], [attackerOutcome[i] for i in range(2, 11)], label="Attacker")
    plt.plot([i for i in range(1, 11)], [defenderOutcome[i] for i in range(1, 11)], label="Defender")
    plt.legend()
    plt.xlabel("Number of Armies Left After Battle")
    plt.ylabel("Probability of Outcome of Armies Left")
    plt.title("Leftover Armies - Starting with 10 Armies")
    plt.show()
