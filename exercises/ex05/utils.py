def only_evens(l1: list[int]) -> list[int]:
    empty = list()
    for item in l1:
        if item % 2 == 0:
            empty.append(item)
    return empty


def sub(l1: list[int], start: int, end: int) -> list[int]:
    result = []
    a = 0
    b = len(l1)
    if start >= 0:
        a = start
    if end <= len(l1):
        b = end

    for i in range(a, b):
        result.append(l1[i])
    return result


def add_at_index(l1: list[int], val_to_add: int, target_index: int) -> None:
    if target_index < 0 or target_index > len(l1):
        raise IndexError

    l1.append(69420)
    for i in range(len(l1) - 1, target_index - 1, -1):
        l1[i] = l1[i - 1]
    l1[target_index] = val_to_add
    return None
