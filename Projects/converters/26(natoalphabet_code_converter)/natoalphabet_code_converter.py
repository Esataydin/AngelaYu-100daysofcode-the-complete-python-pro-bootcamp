import pandas


def nato_alphabet_converter() -> None:
    """"""

    # Creates a dictionary in this format:
    #    {"A": "Alfa", "B": "Bravo"}
    df = pandas.read_csv('nato_phonetic_alphabet.csv')

    phonetic_dict: dict[str, str] = {row.letter: row.code for (index, row) in df.iterrows()}

    # Creates a list of the phonetic code words from a word that the user inputs.
    word: str = input('Enter a word: ').upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        nato_alphabet_converter()
    else:
        print(output_list)


def main() -> None:
    nato_alphabet_converter()


if __name__ == '__main__':
    main()
