from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random
import pygame
from PIL import Image, ImageTk

# Initialize the main window
window = Tk()
window.title('Hangman - GUESS THE WORD')
window.state('zoomed')  # Maximize the window

# Word lists for the Hangman game
city_list = [
    'MUMBAI', 'DELHI', 'BANGALORE', 'HYDERABAD', 'AHMEDABAD', 'CHENNAI', 'KOLKATA', 'SURAT', 'PUNE', 'JAIPUR'
]

fruit_list = [
    'APPLE', 'BANANA', 'CHERRY', 'DATE', 'BLUEBERRY', 'PINEAPPLE', 'GRAPE', 'AVOCADO', 'KIWI', 'ORANGE'
]

adjective_list = [
    'STRATEGY', 'INNOVATIVE', 'FOCUSED', 'RELIABLE', 'BRIGHT', 'ASSERTIVE', 'VERSATILITY', 'PROACTIVE', 'DYNAMIC', 'POSITIVE'
]

sports_list = [
    'CRICKET', 'FOOTBALL', 'BASKETBALL', 'TENNIS', 'RUGBY', 'HOCKEY', 'VOLLEYBALL', 'GOLF', 'BASEBALL', 'SWIMMING'
]

food_list = [
    'PIZZA', 'BURGER', 'PASTA', 'SUSHI', 'SALAD', 'TACOS', 'CURRY', 'ICECREAM', 'BROWNIE', 'DONUT'
]

geographical_list = [
    'CONTINENT', 'ISLAND', 'RIVER', 'MOUNTAIN', 'DESERT', 'OCEAN', 'PLATEAU', 'VOLCANO', 'VALLEY', 'ARCHIPELAGO'
]

technology_list = [
    'COMPUTER', 'PROGRAMMING', 'ALGORITHM', 'SOFTWARE', 'HARDWARE', 'NETWORKING', 'DATABASE', 'CYBERSECURITY', 'ARTIFICIAL_INTELLIGENCE', 'INTERNET'
]

science_list = [
    'ATOM', 'CELL', 'GENE', 'MOLECULE', 'FORCE', 'ENERGY', 'EQUATION', 'CHEMICAL', 'REACTION', 'PHYSICS'
]

# Load images representing hangman stages
photos = [PhotoImage(file=f"images/hang{i}.png") for i in range(12)]

# Initialize pygame for sound effects
pygame.mixer.init()
wrong_guess_sound = pygame.mixer.Sound("sounds/wrong_guess.wav")

# Load background image and convert it to a PhotoImage
background_image = Image.open("images/background.jpg")
background_photo = ImageTk.PhotoImage(background_image)

# Global variables
word_list = []
the_word_withSpaces = ""
numberOfGuesses = 0
score = 0

# Function to start a new game
def newGame():
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses = 0
    the_word = random.choice(word_list)
    the_word_withSpaces = " ".join(the_word)
    lblWord.set(' '.join("_" * len(the_word)))
    imgLabel.config(image=photos[0])
    remainingGuessesLabel.set(f"Remaining Guesses: {11 - numberOfGuesses}")

# Function to handle guessing a letter
def guess(letter):
    global numberOfGuesses
    global score
    if numberOfGuesses < 11:
        txt = list(the_word_withSpaces)
        guessed = list(lblWord.get())
        if the_word_withSpaces.count(letter) > 0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guessed[c] = letter
            lblWord.set("".join(guessed))
            if lblWord.get() == the_word_withSpaces:
                score += 10  # Increase score for a correct guess
                scoreLabel.set(f"Score: {score}")
                messagebox.showinfo("Hangman", "You guessed it!")
                newGame()
        else:
            numberOfGuesses += 1
            imgLabel.config(image=photos[numberOfGuesses])
            remainingGuessesLabel.set(f"Remaining Guesses: {11 - numberOfGuesses}")
            wrong_guess_sound.play()  # Play sound on wrong guess
            if numberOfGuesses == 11:
                score -= 5  # Decrease score for a wrong guess
                scoreLabel.set(f"Score: {score}")
                messagebox.showwarning("Hangman", f"Game Over! The word was {the_word_withSpaces.replace(' ', '')}")
                newGame()

# Function to set the word list based on the selected category
def setCategory():
    global word_list
    selected_category = category.get()
    if selected_category == "Cities":
        word_list = city_list
    elif selected_category == "Fruits":
        word_list = fruit_list
    elif selected_category == "Adjectives":
        word_list = adjective_list
    elif selected_category == "Sports":
        word_list = sports_list
    elif selected_category == "Foods":
        word_list = food_list
    elif selected_category == "Geographics":
        word_list = geographical_list
    elif selected_category == "Technology":
        word_list = technology_list
    elif selected_category == "Science":
        word_list = science_list
    newGame()

# Create a canvas to hold the background image
canvas = Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight())
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor=NW, image=background_photo)

# Create a frame to center the content
centerFrame = Frame(window, bg='#add8e6')
centerFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Create the main image label
imgLabel = Label(centerFrame, bg='#add8e6')
imgLabel.grid(row=0, column=0, columnspan=9, padx=10, pady=10)

# Create the word display label
lblWord = StringVar()
Label(centerFrame, textvariable=lblWord, font=('consolas 24 bold'), bg='#add8e6').grid(row=1, column=0, columnspan=9, padx=10)

# Create label for remaining guesses
remainingGuessesLabel = StringVar()
Label(centerFrame, textvariable=remainingGuessesLabel, font=('Helvetica 14'), bg='#add8e6').grid(row=2, column=0, columnspan=9, pady=(0, 20))

# Create label for score
scoreLabel = StringVar()
scoreLabel.set(f"Score: {score}")
Label(centerFrame, textvariable=scoreLabel, font=('Helvetica 14'), bg='#add8e6').grid(row=3, column=0, columnspan=9, pady=(0, 20))

# Create the category selection radio buttons
categoryFrame = Frame(centerFrame, bg='#add8e6')
categoryFrame.grid(row=4, column=0, columnspan=9, pady=(0, 20))
category = StringVar(value="Cities")
Radiobutton(categoryFrame, text="Cities", variable=category, value="Cities", command=setCategory, font=('Helvetica 14'), bg='#add8e6').pack(side=LEFT, padx=10)
Radiobutton(categoryFrame, text="Fruits", variable=category, value="Fruits", command=setCategory, font=('Helvetica 14'), bg='#add8e6').pack(side=LEFT, padx=10)
Radiobutton(categoryFrame, text="Adjectives", variable=category, value="Adjectives", command=setCategory, font=('Helvetica 14'), bg='#add8e6').pack(side=LEFT, padx=10)
Radiobutton(categoryFrame, text="Sports", variable=category, value="Sports", command=setCategory, font=('Helvetica 14'), bg='#add8e6').pack(side=LEFT, padx=10)
Radiobutton(categoryFrame, text="Foods", variable=category, value="Foods", command=setCategory, font=('Helvetica 14'), bg='#add8e6').pack(side=LEFT, padx=10)
Radiobutton(categoryFrame, text="Geographics", variable=category, value="Geographics", command=setCategory, font=('Helvetica 14'), bg='#add8e6').pack(side=LEFT, padx=10)
Radiobutton(categoryFrame, text="Technology", variable=category, value="Technology", command=setCategory, font=('Helvetica 14'), bg='#add8e6').pack(side=LEFT, padx=10)
Radiobutton(categoryFrame, text="Science", variable=category, value="Science", command=setCategory, font=('Helvetica 14'), bg='#add8e6').pack(side=LEFT, padx=10)

# Create buttons for each letter in the alphabet
keyboardFrame = Frame(centerFrame, bg='#add8e6')
keyboardFrame.grid(row=5, column=0, columnspan=9)
n = 0
for c in ascii_uppercase:
    Button(keyboardFrame, text=c, command=lambda c=c: guess(c), font=('Helvetica 18'), width=4).grid(row=n//9, column=n%9)
    n += 1

# Create the New Game button
Button(centerFrame, text="New\nGame", command=newGame, font=("Helvetica 10 bold")).grid(row=6, column=0, columnspan=9, pady=20)

# Start the game with the default category
setCategory()

# Run the main loop
window.mainloop()