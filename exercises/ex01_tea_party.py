def tea_bags(people: int) -> int:
    return 2 * people


def treats(people: int) -> int:
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    return 0.5 * tea_count + 0.75 * treat_count


def main_planner(guests: int) -> None:
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
