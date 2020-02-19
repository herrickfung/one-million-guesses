# This stimulation will run 1 million guesses by rounding up the average between upper and lower bound.

import random
import csv
import math

logfile = open("round_up_middle_way.csv", 'w', newline = '')
writer = csv.writer(logfile, delimiter = ',')
writer.writerow(['trial', 'No_of_Guesses', 'Answer', 'GuessList'])

list = []

for i in range(100):
    list.append(i + 1)


def game():
    answer = random.choice(list)
    guesslist = []

    lower = list[0]
    upper = list[-1]

    guess = math.ceil((lower + upper) / 2)
    guesslist.append(guess)

    for j in range(100):

        if guess > answer:
            upper = guess
            guess = math.ceil((lower + upper) / 2)
            guesslist.append(guess)
            j += 1

        elif guess < answer:
            lower = guess
            guess = math.ceil((lower + upper) / 2)
            guesslist.append(guess)
            j += 1

        else:
            save = len(guesslist)
            writer.writerow([(k + 1), save, answer, guesslist])
            break


if __name__ == '__main__':
    for k in range(1000000):
        game()
        k += 1
    logfile.close()
