def input_word() -> str:
    user_input = input("Enter a 5-character word: ")
    if (len(user_input)) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return user_input


def input_letter() -> str:
    user_input = input("Enter a single character: ")
    if (len(user_input)) != 1:
        print("Error: Character must be a single character.")
        exit()
    return user_input


def contains_char(word: str, letter: str) -> None:
    counter: int = 0
    print(f"Searching for {letter} in {word}")
    if word[0] == letter:
        counter += 1
        print(f"{letter} found at index {0}")
    if word[1] == letter:
        counter += 1
        print(f"{letter} found at index {1}")
    if word[2] == letter:
        counter += 1
        print(f"{letter} found at index {2}")
    if word[3] == letter:
        counter += 1
        print(f"{letter} found at index {3}")
    if word[4] == letter:
        counter += 1
        print(f"{letter} found at index {4}")

    if counter == 0:
        print(f"No instances of {letter} found in {word}")
    elif counter == 1:
        print(f"1 instance of {letter} found in {word}")
    else:
        print(f"{counter} instances of {letter} found in {word}")
