#!/usr/bin/python3

input_array = [-2, 2, 5, -11, 6]


def array_max_consecutive_sum(arr):
    max_sum = 0
    current_sum = 0
    for number in arr:
        # use sum of previous value and current or "restart" and use the current number as the new base for calculations
        current_sum = max(number + current_sum, number)
        # update the max sum accordingly if the current sum is now greater
        max_sum = max(max_sum, current_sum)
    print(max_sum)


array_max_consecutive_sum(input_array)
