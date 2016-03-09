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

def check(event):
    global lives
    if lives == 0:
        return
    guess = tbox.get()
    if len(guess) == 1:
        if guess in gletters:
            errorbox.configure(text="You have guessed that alphabet already!")
        else:
            gletters.append(guess)
            if guess in word:
                errorbox.configure(text="Great guess!")
                current = getWordText(gletters, word)
                guessed.configure(text=current)
                if '_' not in current:
                    errorbox.configure(text="You have guessed the word correctly!")
            else:
                errorbox.configure(text="Your alphabet was not in the word!")
                lives -= 1
    else:
        errorbox.configure(text="Please input only one alphabet!")
    tbox.delete(0, 'end')
    llabel.configure(text="Lives left: " + str(lives))
    if lives == 0:
        errorbox.configure("Game Over man! Game over!")
    return

wlist = ['Hangman', 'Wood', 'Trees', 'Fish']
word = random.choice(wlist)
lives = 7
window = tkinter.Tk()
window.wm_title("Hangman Game")
gletters = []
guessed = tkinter.Label(window, text=getWordText(gletters, word))
guessed.pack()
label1 = tkinter.Label(window, text="Enter your guess in the box bellow")
label1.pack()
tbox = tkinter.Entry(window)
tbox.bind("<Return>", check)
tbox.pack()
errorbox = tkinter.Label(window, text="Error Messages come here")
errorbox.pack()
llabel = tkinter.Label(window, text="Lives Left: " + str(lives))
llabel.pack()
window.mainloop()