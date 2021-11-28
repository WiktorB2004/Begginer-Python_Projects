import random


template = 'Hello, {}. My name is {}.'

def get_data():
    return input('Enter 2 words to Mad Libs, separate them with commas: ')


def main():
    inputs = get_data().split(',')
    if len(inputs) == 2:
        print(template.format(*inputs))
    else:
        print("Enter correct number of words")

main()
input("Press enter to close the program")
