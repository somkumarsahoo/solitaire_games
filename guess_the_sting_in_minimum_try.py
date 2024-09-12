#!/usr/bin/env python
# coding: utf-8

# Guess the Combination Game:
# 
# * Game Overview:
# 
# - Game Name: Guess the Combination
# - Game Type: Puzzle
# - Objective: Guess a 6-character combination from the letters A to J
# 
# * Gameplay Instructions
# - The computer generates a random 6-character combination from the letters A to J.
# - The player inputs a 6-character guess.
# - The computer validates the guess and provides feedback in the form of character and position 
# 
# * Scores.
# - The player keeps guessing until they correctly guess the combination.
# 
# * Constraints
# - The combination can contain duplicate characters.
# - The player's guess must be exactly 6 characters long.
# - The player's guess must only contain letters from A to J.
# 
# * Scoring
# - Character Score: Number of characters in the guess that appear in the combination (regardless of position)
# - Position Score: Number of characters in the guess that appear in the correct position in the combination
# 
# * Winning Condition
# - The player correctly guesses the 6-character combination (Position Score of 6)

# In[ ]:


import random

class GuessGame:
    def __init__(self):
        self.combination = random.sample('ABCDEFGHIJ', 6)
        self.attempts = 0

    def validate_guess(self, guess):
        if len(guess) != 6:
            print("Invalid guess. Please enter 6 characters.")
            return False
        if not all(char in 'ABCDEFGHIJ' for char in guess):
            print("Invalid guess. Please use characters A to J only.")
            return False
        return True

    def calculate_scores(self, guess):
        character_score = sum(1 for char in guess if char in self.combination)
        position_score = sum(1 for i, char in enumerate(guess) if char == self.combination[i])
        return {'character': character_score, 'position': position_score}

    def play(self):
        print("I'm thinking of a combination of 6 characters from A to J.")
        print("Guess the combination by entering 6 characters.")
        while True:
            guess = input("Enter your guess: ").upper()
            if not self.validate_guess(guess):
                continue
            scores = self.calculate_scores(guess)
            print(f"Character score: {scores['character']}, Position score: {scores['position']}")
            self.attempts += 1
            if scores['position'] == 6:
                code = ''
                for c in self.combination:
                    code = code + c 
                print(f"Congratulations! You won in {self.attempts} attempts. by predicting my secret combination of characters: {code} ")
                break


# In[ ]:


# Render an instance of the game

game = GuessGame()


# In[ ]:


# Run the game

game.play()


# In[ ]:





# In[ ]:




