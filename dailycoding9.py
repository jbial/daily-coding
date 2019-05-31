

def largest_non_adjacent_sum(arr):
    prev1, prev2, result = 0, 0, 0
    for i in range(len(arr)):
        if i == 0:
            result = arr[0]
        elif i == 1:
            result = max(arr[0], arr[1])
        else:
            result = max(prev1, arr[i] + prev2)
        prev2 = prev1
        prev1 = result

    return result


def main():

    arrs = (
        [9, 0, 9, 0],
        [1, 2, 3, 4],
        [1, 2, 3],
        [2, 8, 1, 9, 0],
        [2, 4, 6, 2, 5],
        [5, 1, 1, 5],
        [5, 0, 0, 8, 0, 6],
        [5, 1, 6, 8, 2, 4],
        [0, 0, 5, 0, 8],
        [5, 5, 5, 5, 5],
    )
    arrs_ans = [18, 6, 4, 17, 13, 10, 19, 17, 13, 15]

    if (arrs_ans == [largest_non_adjacent_sum(arr) for arr in arrs]):
        print("Passed")
    else:
        print("Failed")


if __name__ == '__main__':
    main()
