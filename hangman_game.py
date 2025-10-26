import random

class HangmanGame:
    def __init__(self):
        self.words = ["python", "programming", "computer", "algorithm", "developer"]
        self.secret_word = ""
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.max_attempts = 6
        
    def choose_word(self):
        """Randomly select a word from the list"""
        self.secret_word = random.choice(self.words).lower()
        self.guessed_letters = ["_"] * len(self.secret_word)
        
    def display_word(self):
        """Display the current state of the word"""
        print("Word: " + " ".join(self.guessed_letters))
        print(f"Incorrect guesses left: {self.max_attempts - self.incorrect_guesses}")
        
    def make_guess(self, letter):
        """Process a letter guess"""
        letter = letter.lower()
        
        if letter in self.secret_word:
            # Update guessed letters
            for i, char in enumerate(self.secret_word):
                if char == letter:
                    self.guessed_letters[i] = letter
            print(f"Good guess! '{letter}' is in the word.")
        else:
            self.incorrect_guesses += 1
            print(f"Sorry, '{letter}' is not in the word.")
            
    def is_word_guessed(self):
        """Check if the word has been completely guessed"""
        return "_" not in self.guessed_letters
    
    def play(self):
        """Main game loop"""
        print("🎮 Welcome to Hangman Game!")
        print("=" * 30)
        
        self.choose_word()
        
        while self.incorrect_guesses < self.max_attempts:
            print("\n" + "=" * 30)
            self.display_word()
            
            if self.is_word_guessed():
                print(f"\n🎉 Congratulations! You guessed the word: {self.secret_word}")
                break
                
            guess = input("\nEnter a letter: ").strip()
            
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter!")
                continue
                
            if guess in "".join(self.guessed_letters):
                print("You already guessed that letter!")
                continue
                
            self.make_guess(guess)
            
        else:
            print(f"\n💀 Game Over! The word was: {self.secret_word}")

# Run the game
if __name__ == "_main_":
    game = HangmanGame()
    game.play()