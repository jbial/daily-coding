"""
This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous
subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86],
the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0,
since we would not take any elements.

Do this in O(N) time.

solution:
Use Kadane's algorithm which simply keeps track of the largest contiguous
running segment of the array and an overall max sum.
"""
def max_subarray(arr):
    if not arr or max(arr) < 0:
        return 0

    running_max = overall_max = 0
    for num in arr:
        running_max = max(num, running_max + num)
        overall_max = max(overall_max, running_max)
    return overall_max


def main():

    tests = {
        137: [34, -50, 42, 14, -5, 86],
        0: [-5, -1, -8, -9],
        95: [44, -5, 42, 14, -150, 86],
        7: [-2, -3, 4, -1, -2, 1, 5, -3]
    }
    if all(max_subarray(tests[k]) == k for k in tests):
        print("Passed")
    else:
        print("Failed")


if __name__ == '__main__':
    main()

