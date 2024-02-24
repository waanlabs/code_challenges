from calorie_counter import CalorieCounter


def main() -> None:
    counter = CalorieCounter("./puzzle-input.txt")
    counter.read_and_process()

    print(f"Max group sum: {counter.max_group_sum()}")
    print(f"Sum of largest three: {counter.sum_of_largest_three()}")

if __name__ == "__main__":
    main()
