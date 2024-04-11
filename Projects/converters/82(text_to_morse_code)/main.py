from morse_code_dict import MORSE_CODE_DICT


def main() -> None:
    text: str = input("Enter a text which you want to convert it to morse code:").upper()

    for letter in text:
        if letter == " ":
            print("            ", end="")
        elif letter in MORSE_CODE_DICT:
            print(MORSE_CODE_DICT[letter], "  ", end="")


if __name__ == '__main__':
    main()
