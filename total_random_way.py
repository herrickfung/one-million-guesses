# This code will stimulate 1 million guesses through total randomization within the interval.

import random
import csv

logfile = open("total_random_way.csv", 'w', newline = '')
writer = csv.writer(logfile, delimiter = ',')
writer.writerow(['trial', 'No_of_Guesses', 'Answer'])

list = []

for i in range(100):
	list.append(i + 1)


def game():
	answer = random.choice(list)

	lower = list[0]
	upper = list[-1]

	guess = random.randint(lower, upper)

	for j in range(100):

		if guess > answer:
			upper = guess
			guess = random.randint(lower, upper)
			j += 1

		elif guess < answer:
			lower = guess
			guess = random.randint(lower, upper)
			j += 1

		else:
			save = j + 1
			writer.writerow([(k + 1), save, answer])
			break


if __name__ == '__main__':
	for k in range(1000000):
		game()
		k += 1
	logfile.close()
