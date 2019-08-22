"""
This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in
faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8,
return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.

Solution:
Use rotated binary search to find the index in O(logn)
"""

def index_search(arr, val, start, end):
    """Performs recursive rotated binary search to find the index of val
    """
    mid = start + (end - start) // 2

    if arr[mid] == val:
        return mid
    elif arr[mid] > arr[start]:  # left is sorted
        if arr[start] <= val and val <= arr[mid]:
            return index_search(arr, val, start, mid - 1)
        else:
            return index_search(arr, val, mid + 1, end)
    else:  # right must be sorted otherwise 
        if arr[mid] <= val and val <= arr[end]: 
            return index_search(arr, val, mid + 1, end)
        else:
            return index_search(arr, val, start, mid - 1)


def argval(arr, val):
    """Main function for rotated binary search
    """
    return index_search(arr, val, 0, len(arr) - 1)


def main():

    tests = [
        [13, 18, 25, 2, 8, 10],
        [10, 13, 18, 25, 2, 8],
        [18, 25, 2, 8, 10, 13]
    ]

    if all(all(argval(t, num) == i for i, num in enumerate(t)) for t in tests):
        print("Passed")
    else:
        print("Failed")


if __name__ == '__main__':
    main()

