"""
This problem was asked by Google.

We can determine how "out of order" an array A is by counting the number
of inversions it has. Two elements A[i] and A[j] form an inversion
if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has.
Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

solution:
Do merge sort but keep track of how many inversions take place i.e. how many times
a[i] is swapped with a[j] when merging the sorted arrays when a[i]>a[j], i<j.
"""
def merge(a_with_inv, b_with_inv):
    i, j = 0, 0
    a, a_inv = a_with_inv
    b, b_inv = b_with_inv
    inv = a_inv + b_inv
    merged = list()

    # merge the sorted arrays
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:  # inversion required
            merged.append(b[j])
            inv += len(a[i:])
            j += 1
    # fill any remaining
    while i < len(a):
        merged.append(a[i])
        i += 1
    while j < len(b):
        merged.append(b[j])
        j += 1
    return merged, inv


def mergesort(arr):
    if not arr or len(arr) == 1:
        return arr, 0

    mid = len(arr) // 2
    merged_arr, inv = merge(
        mergesort(arr[:mid]), mergesort(arr[mid:]))

    return merged_arr, inv 


def count_inversions(arr):
    _, inversions = mergesort(arr)
    return inversions


def main():

    tests = {
        0: [1,2,3,4],
        1: [2,1,3,4],
        2: [2,3,1,4],
        3: [3,2,1,4],
        4: [5,1,4,2]
    }

    if all(count_inversions(tests[k]) == k for k in tests):
        print("Passed")
    else:
        print("Failed")


if __name__ == '__main__':
    main()
