"""
This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned into
two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10},
it would return true, since we can split it up into {15, 5, 10, 15, 10} and
{20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false,
since we can't split it up into two subsets that add up to the same sum.

Solution:
Sort the nums and greedily search for the sum // 2, if found, then return True.
Runs in O(n^2)
"""

def can_partition(nums):
    if len(nums) == 0:
        return False

    tot, size = sum(nums), len(nums)
    if tot % 2 == 1:
        return False

    # Sort the list in reverse and greedily search for the target
    target = tot // 2
    nums.sort(reverse=True)
    for i in range(size):
        temp = 0
        for j in range(i, size):
            if temp + nums[j] == target:
                return True
            elif temp + nums[j] < target:
                temp += nums[j]
    return False


def main():

    tests = (
        ([15, 5, 20, 10, 35], False),
        ([15, 5, 20, 10, 35, 15, 10], True),
        ([10, 4], False),
        ([4, 1, 5], True),
        ([9, 3, 1], False)
    )
    
    if all(can_partition(k) == test for k, test in tests):
        print("Passed")
    else:
        print("Failed")


if __name__ == '__main__':
    main()

