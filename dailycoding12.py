def count_steps_rec(n, x, memo):
    """Recursively count the steps from the set on each step
    """
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    if n < 0:
        return 0

    # store the result in the mem table
    result = sum(count_steps_rec(n - k, x, memo) for k in x)
    memo[n] = result
    return result


def count_steps(n, x):
    """Count steps with memoization
    """
    return count_steps_rec(n, x, {})


def main():

    tests = {
        5: (5, {1, 3, 5}),
        23: (7, {1, 2, 6}),
        1: (4, {1}),
        13: (6, {1, 2})
    }
    if all(k == count_steps(*tests[k]) for k in tests):
        print("Passed")
    else:
        print("Failed")

if __name__ == '__main__':
    main()
