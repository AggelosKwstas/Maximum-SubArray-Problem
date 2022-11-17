def brute_force(a_list):
    max = a_list[0]
    start, end = 0, 0
    for i in range(len(a_list)):
        for j in range(i, len(a_list)):
            sum = 0
            for x in range(i, j + 1):
                sum += a_list[x]
            if max < sum:
                max, start, end = sum, i, j

    return "max is: " + str(max) + "      " + "start index is : " + str(start) + "      " + "end index is : " + str(end)


def calculate_prefix(test_list):
    size = len(test_list)
    res = [0] * size
    res[0] = test_list[0]
    max_sum, start, end = test_list[0], 0, 0
    for i in range(1, len(test_list)):
        res[i] = res[i - 1] + test_list[i]

    for i in range(len(test_list)):
        for j in range(i, len(test_list)):
            sum = res[j] if i == 0 else res[j] - res[i - 1]

            if max_sum < sum:
                max_sum, start, end = sum, i, j

    return "max is: " + str(max_sum) + "      " + "start index is : " + str(start) + "      " + "end index is : " + str(
        end)


def calculate_kadane(a_list):
    kadane_table = list()
    start = 0
    for index, num in enumerate(a_list):
        if index == 0:
            sum = num
        else:
            sum = num + kadane_table[index - 1]
        kadane_table.append(0 if sum < 0 else sum)

    max_val = max(kadane_table)
    max_index = kadane_table.index(max_val)

    for i in reversed(range(max_index)):
        if kadane_table[i] == 0:
            start = i + 1
            break

    return "max is: " + str(max_val) + "      " + "start index is : " + str(start) + "      " + "end index is : " + str(
        max_index)
