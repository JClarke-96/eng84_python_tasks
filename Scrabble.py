class ScrabbleCalculator:

    def __init__(self):
        self.letter_score = {"A": 1, "E": 1, "I": 1, "O": 1, "U": 1,    # Set up dictionary with letters and their scores
                             "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
                             "D": 2, "G": 2,
                             "B": 3, "C": 3, "M": 3, "P": 3,
                             "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
                             "K": 5,
                             "J": 8, "X": 8,
                             "Q": 10, "Z": 10
                             }
        self.word = ""      # Set up word with no default, later overwrite
        self.score = 0      # Set up score with no points, later overwrite

    def calculate_score(self, word):
        for letter in word:     # Loop through each letter in the word
            self.score += self.letter_score[letter]     # Update score each letter to add that letter's score

        print(f"{word} is worth {self.score} points")   # Print score for the word
        self.reset()

    def reset(self):        # Reset the score each time it has been printed
        self.score = 0


if __name__ == "__main__":
    calc = ScrabbleCalculator()
    new_word = True
    while new_word:         # Keep inputting new words to calculate their score
        print("Scrabble word score calculator!")
        word = input("Please input a word:  ").upper()
        if word == "BREAK": # BREAK to escape from the code after finishing
            new_word = False
            break
        calc.calculate_score(word)
