# This stimulation will run 1 million guesses by rounding off the average between upper and lower bound.

import random
import csv

logfile = open("middle_way.csv", 'w', newline = '')
writer = csv.writer(logfile, delimiter = ',')
writer.writerow(['trial', 'No_of_Guesses', 'Answer'])

list = []

for i in range(100):
	list.append(i + 1)


def game():
	answer = random.choice(list)

	lower = list[0]
	upper = list[-1]

	guess = round((lower + upper) / 2)

	for j in range(100):

		if guess > answer:
			upper = guess
			guess = round((lower + upper) / 2)
			j += 1

		elif guess < answer:
			lower = guess
			guess = round((lower + upper) / 2)
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
