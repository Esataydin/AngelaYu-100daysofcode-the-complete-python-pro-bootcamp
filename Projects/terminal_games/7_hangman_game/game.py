import random

import hangman_art as hga
import hangman_words as hgw


def main() -> None:
    print(hga.logo)
    end_of_game = False
    chosen_word = random.choice(hgw.word_list)
    word_length = len(chosen_word)


    lives = 6

    display = []
    #Creates blanks
    for _ in range(word_length):
        display += "_"
    print(f"{' '.join(display)}")

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        #Checks guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        #Decreases lives by 1 If guess is not a letter in the chosen_word,
        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1

        # If lives goes down to 0 then the game should stop and it should print "You lose."
        print(hga.stages[lives])
        #Joins all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        #Checks if user has got all letters.
        if lives == 0:
            end_of_game = True
            print(f"The word was: {chosen_word}")
            print("You lose.")
        if "_" not in display:
            end_of_game = True
            print("You win.")


if __name__ == '__main__':
    main()
