from calorie_counter import CalorieCounter


def main() -> None:
    calorie_counter = CalorieCounter("./puzzle-input.txt")
    calorie_counter.read_and_process()

    print(f"Max group sum: {calorie_counter.max_group_sum()}")
    print(f"Sum of largest three: {calorie_counter.sum_of_largest_three()}")


if __name__ == "__main__":
    main()
