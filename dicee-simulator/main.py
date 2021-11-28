import random

def main():
    dices_num = int(input('How many dicees do you want to throw? '))
    for x in range(0, dices_num):
        print(f'Dicee {x + 1}: ', random.randint(1,6))
    
main()
input("Press enter to close the program")