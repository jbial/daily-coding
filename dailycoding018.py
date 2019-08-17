
def max_subarray(arr, k):
    start = 0
    end = k - 1
    ret = ""
    while end < len(arr):
        ret += str(max(arr[start:end + 1])) + " "
        start += 1
        end += 1
    print(ret)


def main():

    tests = (
        ([10, 5, 2, 7, 8, 7], 3),
        ([9, 2, 4, 13, 5, 6, 1, 35], 4),
        ([3, 5, 3, 7, 4, 8, 4, 7, 5], 2),
        ([1, 2, 3, 1, 4, 5, 2, 3, 6], 3),
        ([8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4),
        ([12, 1, 78, 90, 57, 89, 56], 3)
    )
    test_num = 5
    print(f"input array: {tests[test_num][0]}")
    max_subarray(*tests[test_num])


if __name__ == '__main__':
    main()
