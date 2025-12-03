# Use to switch between parts so you don't have to comment/uncomment code
PART = 1

# Part 1
if PART == 1:

    # Combination order
    with open("inputs/day_01_input_01.txt", "r") as f:
        combination_order = [line.strip() for line in f]

    # Function to count the number of times the combination landed on zero
    def count_zeros(input_list: list) -> int:

        counter = 0
        index = 50
        step = 0

        for item in input_list:

            if item.startswith("L"):
                step = int(item[1:])
                index = index - step
            else:
                step = int(item[1:])
                index = index + step

            if index % 100 == 0:
                counter += 1

        return counter

    print(count_zeros(combination_order)) # The answer is 980

# Part 2