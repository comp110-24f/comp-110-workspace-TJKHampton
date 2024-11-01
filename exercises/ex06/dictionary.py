def invert(dictionary: dict[str, str]) -> dict[str, str]:
    result = dict()
    for key in dictionary:
        current_value: str = dictionary[key]
        if current_value in result:
            raise KeyError()
        else:
            result[current_value] = key
    return result


# from exercises.ex06.dictionary import invert


def favorite_color(dictionary: dict[str, str]) -> str:
    counter: dict[str, int] = dict()
    for key in dictionary:
        current_value: str = dictionary[key]
        if current_value in counter:
            counter[current_value] += 1
        else:
            counter[current_value] = 1

    big_color = ""
    max_num = 0
    for key in counter:
        if counter[key] > max_num:
            max_num = counter[key]
            big_color = key
    return big_color


def count(l1: list[int]) -> dict[str, int]:
    result = dict()
    for item in l1:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result


def alphabetizer(l1: list[str]) -> dict[str, list[str]]:
    result = dict()
    for item in l1:
        first_char = item[0].lower()
        if first_char in result:
            result[first_char].append(item)
        else:
            result[first_char] = list()
            result[first_char].append(item)
    return result


def update_attendance(d1: dict[str, list[str]], day: str, name: str) -> None:
    if day in d1:
        d1[day].append(name)
    else:
        d1[day] = list()
        d1[day].append(name)
