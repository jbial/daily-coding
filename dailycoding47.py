"""
This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in
chronological order, write a function that calculates the maximum profit
you could have made from buying and selling that stock once.
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5,
since you could buy the stock at 5 dollars and sell it at 10 dollars.

solution:
If plotted as a time series, the maximum profit corresponds to the difference
between the lowest valley and the highest peak. So we can keep track of the
min price and max difference as variables and find the max profit in one pass.
"""

def maximum_profit(index):
    """Finds the maximum profit in one pass
    """
    if not index or len(index) < 2:
        return

    min_price = index[0]
    max_diff = -1e99
    for price in index[1:]:
        if price - min_price > max_diff:
            max_diff = price - min_price
        if price < min_price:
            min_price = price
    return max_diff


def main():

    tests = {
        5: [9,11,8,5,7,10],
        4: [1,2,3,4,5],
        0: [1,1,1],
        1: [1,1,2,1],
        -1: [5,4]
    }

    if all(maximum_profit(tests[k]) == k for k in tests):
        print("Passed")
    else:
        print("Failed")


if __name__ == '__main__':
    main()
