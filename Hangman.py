import random
import tkinter

def getWordText(letters, word):
    wordtext = ""
    for letter in word:
        if letter in letters:
            wordtext += letter
        else:
            wordtext += "_ "
    return wordtext

wlist = ['Hangman', 'Wood', 'Trees', 'Fish']
word = random.choice(wlist)
window = tkinter.Tk()
window.wm_title("Hangman Game")
gletters = []
guessed = tkinter.Label(window, text = getWordText(gletters, word))
guessed.pack()
finish = False
window.update_idletasks()
window.update()
while finish == False:
    while True:
        guess = input("Enter your guessed alphabet: ")
        if len(guess) == 1:
            if guess in gletters:
                print("You have guessed that alphabet already!")
            else:
                gletters.append(guess)
                if guess in word:
                    print("Great guess!")
                    current = getWordText(gletters, word)
                    guessed.configure(text = current)
                    window.update_idletasks()
                    window.update()
                    if '_' not in current:
                        print("You have guessed the word correctly!")
                        finish = True
                        break
                else:
                    print("Your alphabet was not in the word!")
                break
        else:
            print("Please input only one alphabet!")
