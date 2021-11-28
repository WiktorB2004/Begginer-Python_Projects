import os

# What to add: Scoring system

def clearConsole():
    command = 'clear'
    os.system(command)

class Player:
    def __init__(self, name):
        self.name = name
        
def getPlayers():
    global p1,p2
    p1 = Player(input("Enter player 1 name, this one will choose word to guess: "))
    p2 = Player(input("Enter player 2 name, this one is a guesser: "))
    
def round():
    turn = 1
    print(f'It`s {p1.name}`s turn')
    word = input(f'Enter the word to guess for {p2.name}: ').lower()
    if not word.isalpha():
        print('Enter the correct type --> word made only of letters')
        word = input(f'Enter the WORD to guess for {p2.name}: ')
    clearConsole()
    guessWord(word)

def guessWord(word):
    lives = 11
    correct_tries = []
    failed_tries = []
    print(f'Guess the word')
    printWord(correct_tries, word)
    while len(failed_tries) < 11:
        print(f'\nLives left {lives - len(failed_tries)}')
        guess = input('\nGuess the LETTER: ')
        if guess.lower() in word and len(guess) == 1:
            print('\nWELL DONE\n')
            correct_tries.append(guess)
            clearConsole()
        else: 
            print('\nTRY AGAIN\n')
            failed_tries.append(guess)
            clearConsole()
        if printWord(correct_tries, word):
            break

def printWord(letters, word):
    w = list('_'*len(word))
    for x in letters:
        if x in word:
            w[word.index(x)] = x
    print(''.join(w))
    if compare(w,word):
        return True
    

def compare(w , word):
    if ''.join(w) == word:
        print('\nYou guessed the word, CONGRATULATIONS\n')
        return True
    

def main():
    getPlayers()
    round()
    
main()
input('Click enter to exit...')