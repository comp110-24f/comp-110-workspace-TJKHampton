def all(lst: list[int], target: int) -> bool:
    idx: int = 0
    while idx < len(lst):
        if lst[idx] != target:
            return False
        idx += 1
    return True


def max(lst: list[int]) -> int:
    if len(lst) == 0:
        raise ValueError

    found_max: int = lst[0]
    idx: int = 1
    while idx < len(lst):
        if lst[idx] > found_max:
            found_max = lst[idx]
        idx += 1
    return found_max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):
        return False
    idx: int = 0
    while idx < len(list2):
        if list2[idx] != list1[idx]:
            return False
        idx += 1

    return True


def extend(list1: list[int], list2: list[int]) -> None:
    for elem in list2:
        list1.append(elem)
    return
