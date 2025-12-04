# Part 1

# Order of inputs
with open("inputs/day_01_input.txt", "r") as f:
    combination_order = [line.strip() for line in f]

# Function to count the number of times the combination landed on zero
def count_zeros(input_list: list) -> int:

    counter = 0
    index = 50
    step = 0

    for item in input_list:

        step = int(item[1:])

        if item.startswith("L"):
            index = index - step
        else:
            index = index + step

        if index % 100 == 0:
            counter += 1

    return counter

# Answer
answer_1 = count_zeros(combination_order)
print(f"The answer to part 1 is: {answer_1}")

# Part 2

# This time adding functionality to also count if dial passed through zero
def count_zeros_and_between(input_list: list) -> int:

    counter = 0
    index = 50
    step = 0

    for item in input_list:

        step = int(item[1:])

        if item.startswith("L"):
            index = index - step
        else:
            index = index + step

        if index % 100 == 0:
            counter += 1

    return counter

# Answer
answer_2 = count_zeros_and_between(combination_order)
print(f"The answer to part 2 is: {answer_2}")