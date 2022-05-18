import random


def write(word_write):
    foo = open("dictionary.txt", "a")
    foo.write(word_write+"\n")
    foo.close()

def read():
    foo = open("dictionary.txt", "r")
    word_read = foo.readlines()
    foo.close()
    return word_read

def wordsel(list_words):
    return random.choice(list_words)

def user_entry(word_choice):
    for i in range(0, (len(word_choice)-1)):
        lives = 0
        letter = input("enter the letter of the word\n")
        if letter == word_choice[i]:
            print("congragulations you got it right")
        else:
            print("you failed")
            while letter != word_choice[i]:
                lives += 1
                letter = input("enter the letter of the letter again\n")
                if letter == word_choice[i]:
                    print("congragulations you got it right")
                if lives == 3:
                    break
                return lives
        if lives == 3:
            break
    print("the word was " + word_choice)

def start():
    list_words = read()
    print(wordsel(list_words))
    word_choosen = wordsel(list_words)
    user_entry(word_choosen)

# we need to specify how many times we want to enter a new word to the system
def start_withvalues():
    for i in range(0, 5):
        m = input("enter a word that you wish should be here\n")
        write(m)
    start()
    continue_choice = input("do you want to continue with the game(y for yes and n for no)")
    if continue_choice == 'y':
        start()
        continue_choice = input("do you want to continue with the game(y for yes and n for no)")
        while continue_choice == 'y':
            start()
            if continue_choice == 'n':
                quit()
    else:
        quit()
# we want to give the choice of whether to start by enterring the data or just go ahead with the game
def start_withoutvalues():
    start()
    continue_choice = input("do you want to continue with the game(y for yes and n for no)")
    if continue_choice == 'y':
        start()
        continue_choice = input("do you want to continue with the game(y for yes and n for no)")
        while continue_choice == 'y':
            start()
            if continue_choice == 'n':
                quit()
    else:
        quit()

# now lets start the game
start_entry = input("tell us how you wish to start(enter only numbers)\n1. start by entering your values\n2. start by entering the values in the system\n3. exit the game")
if start_entry == 1:
    start_withvalues()
elif start_entry == 2:
    start_withoutvalues()
else:
    quit()    