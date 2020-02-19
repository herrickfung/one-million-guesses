# This is the original game to select an integer between 1 to 100
import random


def game():
    list = []
    for j in range(100):
        list.append(j + 1)

    answer = random.choice(list)

    lower = list[0]
    upper = list[-1]

    guess = input("Enter a Number between " + str(lower) + " to " + str(upper) + ": ")
    

    try:
        guess = int(guess)
    except:
        print("Learn what is a number and come back later!")
        return 0

    for i in range(100):

        try:
            guess = int(guess)
        except:
            print("Learn what is a number and come back later!")
            break

        if guess > upper or guess < lower:
            print("Out of range")
            guess = input("Try Again, Enter a Number between " + str(lower) + " to " + str(upper) + ": ")
            i += 1

        elif guess > answer:
            print("Too Big")
            upper = guess
            guess = input("Try Again, Enter a Number between " + str(lower) + " to " + str(upper) + ": ")
            i += 1

        elif guess < answer:
            print("Too Small")
            lower = guess
            guess = input("Try Again, Enter a Number between " + str(lower) + " to " + str(upper) + ": ")
            i += 1

        else:
            print("You win, You have guessed the number in " + str(i + 1) + " times.")
            break


if __name__ == '__main__':
    while True:
        game()
        resp = input("Do you want to play again (y/n): ")
        if resp == 'y':
            continue
        else:
            print("See you!")
            break
