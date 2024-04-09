import random
import string

from words import words


def get_valid_word(words_frm_import):
    word = random.choice(words_frm_import)  # randomly chooses something from the words list
    while '-' in word or ' ' in word:
        word = random.choice(words_frm_import)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) -> 'a b cd'
        print(f"You have {lives} lives left & you used these letters: ".join(used_letters))

        # what current word is (i.e. W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1  # decrementing player lives
                print(f'{user_letter} is not in word.')

        elif user_letter in used_letters:
            print("You've already used that character. Please retry. ")

        else:
            print("Invalid character. Please retry.")

    # get here when len(word_letters) == 0 OR when lives == 0
    print(f"You've guessed the word: {word}!!")


hangman()
user_input = input("Type something: ")
print(user_input)
