"""
Given a list of integers S and a target number k,
write a function that returns a subset of S that adds up to k.
If such a subset cannot be made, then return null.

Integers can appear more than once in the list.
You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24,
return [12, 9, 2, 1] since it sums up to 24.

solution:

Use divide and conquer by considering subproblems of the array with k <- k - s[0].
If a solution exists for that subproblem, then s[0] is in the solution set and 
recurse further, otherwise, recurse on the next subproblem with the sum unchanged.

Runs in O(N) time, O(N) space
"""
def subset_sum(s, k):
    # base cases
    if len(s) == 0:
        return None
    if s[0] == k:
        return [s[0]]

    # if the subproblem can be solved with the first element,
    # then return the first element + the solution to the subproblem.
    # Otherwise the first element is not in the solution, so solve the sub
    # problem with the same current sum.
    subsum = subset_sum(s[1:], k - s[0])
    if subsum:
        return [s[0]] + subsum
    else:
        return subset_sum(s[1:], k)


def main():

    tests = (
        ([12, 1, 61, 5, 9, 2], 24),
        ([12, 1, 61, 5, 9, 2], 61),
        ([12, 1, 61, 5, -108, 2], -106),
        ([1,2,3], 40)
    )
    ans = (
        [12, 1, 9, 2],
        [61],
        [-108, 2],
        None
    )

    if all(subset_sum(*t) == a for t, a in zip(tests, ans)):
        print("Passed")
    else:
        print("Failed")

if __name__ == '__main__':
    main()
