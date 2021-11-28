import random 

lives = 3
number = int(random.randrange(1,10))


def main():
    global lives
    user_num = guessNum()
    while lives != 1:
        if compareNumbers(user_num, number):
            print("You guessed correctly. Congratulations!!!")
            return 0
        else:
            lives -= 1
            print(give_hint(lives))
            print(f'You guessed wrong! and you got {lives} lives')
            user_num = guessNum()
    return 0

def guessNum():
    return input(f'Enter the number between 1 and 10, you have {lives} lives left and you will get hint after failed guess: ')

def compareNumbers(user_num, number):
    if int(user_num) == number:
        return True
    return False

def give_hint(i):
    isGreater = number > 5
    isEven = number % 2 == 0
    if i == 2 or 1:
        return f'Your number is greater than five: {isGreater}'
    if i == 1:
        return f'Your number is divisible by 2: {isEven}'


main()
input("Press enter to close the program")