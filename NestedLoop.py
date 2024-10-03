def find_max(numbers):

    big = numbers[0]
    for item in numbers:
        if big < item:
            big =item
    print(big)