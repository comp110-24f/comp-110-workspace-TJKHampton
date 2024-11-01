def input_guess(secret_word_len: int) -> str:
    guess: str = input("Enter a 5 character word: ")
    while len(guess) != 5:
        guess = input("That wasn't 5 chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    assert len(char_guess) == 1

    count: int = 0
    while count < len(secret_word):
        if secret_word[count] == char_guess:
            return True
        count += 1
    return False


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    count: int = 0
    result: str = ""
    while count < len(guess):
        current_char: str = guess[count]
        if contains_char(secret_word=secret, char_guess=current_char):
            if current_char == secret[count]:
                result += GREEN_BOX
            else:
                result += YELLOW_BOX
        else:
            result += WHITE_BOX
        count += 1

    return result


def main(secret: str):
    turn_count: int = 1
    while turn_count <= 6:
        print(f"=== Turn {turn_count}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess=guess, secret=secret))
        if guess == secret:
            print(f"You won in {turn_count}/6 turns!")
            return
        turn_count += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
