class ScrabbleCalculator:

    def __init__(self):
        self.letter_score = {"A": 1, "E": 1, "I": 1, "O": 1, "U": 1,
                             "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
                             "D": 2, "G": 2,
                             "B": 3, "C": 3, "M": 3, "P": 3,
                             "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
                             "K": 5,
                             "J": 8, "X": 8,
                             "Q": 10, "Z": 10
                             }
        self.word = ""
        self.score = 0

    def calculate_score(self, word):
        self.word = word

        for letter in word:
            self.score += self.letter_score[letter]

        print(f"{word} is worth {self.score} points")
        self.reset()

    def reset(self):
        self.score = 0


if __name__ == "__main__":
    calc = ScrabbleCalculator()
    new_word = True
    while new_word:
        print("Scrabble word score calculator!")
        word = input("Please input a word:  ").upper()
        if word == "BREAK":
            new_word = False
            break
        calc.calculate_score(word)
