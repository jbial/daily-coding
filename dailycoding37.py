"""
This problem was asked by Google.

The power set of a set is the set of all its subsets. 
Write a function that, given a set, generates its power set.

solution:
Use a divide and conquer approach by recusively including all subsets
missing one element from the original set, e.g.
{1,2,3} ->
    {2,3} ->
        {2}, {3}
    {1,3} ->
        {1}, {3}
    {1,2} ->
        {1}, {2}
To avoid adding duplicates to power set, use the powerset as a memoization
table, passing it along every recursion and only adding to it if a subset
is not already in it.

Runs in O(2^N) time since that is the cardinality of the power set

"""

def subset(nums, k, size):
    return [nums[i] for i in range(size) if i != k]


def powerset_rec(nums, pset):
    if set(nums) in pset:
        return
    pset.append(set(nums))
    for i in range(len(nums)):
        s = subset(nums, i, len(nums))
        powerset_rec(s, pset)


def powerset(nums):
    pset = []
    powerset_rec(list(nums), pset)
    return pset

def main():

    tests = (
        (set(), [set()]),
        ({1,2,3}, [set(),{1},{2},{3},{1,2},{2,3},{1,3},{1,2,3}]),
        ({1}, [set(), {1}]),
        ({1,2}, [set(), {1,2}, {1}, {2}])
    )

    if all([s in t[1] for s in powerset(t[0])] for t in tests):
        print("Passed")
    else:
        print("Failed")


if __name__ == '__main__':
    main()
