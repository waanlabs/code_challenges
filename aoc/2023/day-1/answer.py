import re


def words_to_numbers(s):
    # Mapping of number words to their numeric values
    num_words = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10  # You can extend this dictionary as needed
    }

    # Find all words in the string
    words = re.findall(r'\b\w+\b', s)

    # Filter words that are number words
    number_words = [word for word in words if word.lower() in num_words]

    # Check if we have at least one number word
    if not number_words:
        return "No number words found"

    # Convert the first and last number words to numbers
    first_num = num_words[number_words[0].lower()]
    last_num = num_words[number_words[-1].lower()]

    # Concatenate and return the result
    return str(first_num) + str(last_num)


# Example usage
s = "two1nine"
result = words_to_numbers(s)
print(result)  # Expected output: "29"
