# This code will stimulate 1 million guesses by control randomization without repeating guesses.

import random
import csv

logfile = open("non_repeat_control_random_way.csv", 'w', newline = '')
writer = csv.writer(logfile, delimiter = ',')
writer.writerow(['trial', 'No_of_Guesses', 'Answer', 'GuessList'])

list = []

for i in range(100):
    list.append(i + 1)


def game():
    guesslist = []
    answer = random.choice(list)

    lower = list[0]
    upper = list[-1]

    guess = random.randint(lower, upper)
    guesslist.append(guess)

    for j in range(100):

        if guess > answer:
            upper = guess
            guess = random.randint(lower, upper)

            if guess in guesslist:
                pass

            else:
                guesslist.append(guess)
                j += 1

        elif guess < answer:
            lower = guess
            guess = random.randint(lower, upper)

            if guess in guesslist:
                pass

            else:
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
