
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python using loops, conditionals, and string operations. By the end of this assignment, you will create an interactive terminal game that tracks guesses and game state correctly.

## 📝 Tasks

### 🛠️	Set Up Core Game Data

#### Description
Create the basic data structures and setup logic for your Hangman game. Define a list of possible words, randomly choose one secret word, and initialize the values needed to track guesses and remaining attempts.

#### Requirements
Completed program should:

- Define a predefined list of possible words.
- Randomly select one word as the secret word at the start of the game.
- Initialize a collection to store guessed letters.
- Initialize a counter for incorrect guesses remaining.


### 🛠️	Implement Gameplay Loop and End Conditions

#### Description
Build the main game loop that repeatedly asks the player for a letter, updates progress, and checks whether the player has won or lost.

#### Requirements
Completed program should:

- Accept one letter guess per turn from user input.
- Display current word progress using underscores for unknown letters (for example: `_ a _ _ m a _`).
- Decrease remaining attempts only when a guessed letter is not in the secret word.
- End the game with a clear win message when all letters are guessed.
- End the game with a clear lose message when attempts reach zero.
