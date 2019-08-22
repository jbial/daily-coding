"""
This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function,
where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.

Solution:
Use the binary exponentiation algorithm, where the answer is the product of the 
on-bits in the exponent e.g. 3^9 = 3^(1*2^3 + 0*2^2 + 0*2^1 + 1*2^0) = (3^8)3

This way the function runs in O(logn) since there are logn bits 
in an n digit base-10 number
"""

def pow(a, b):
    res = 1
    while b > 0:
        # if the bit is on, update the result
        if b & 1:
            res *= a
        # update the next product and right shift the exponent
        a *= a
        b >>= 1
    return res


def main():

    tests = [(3, 9), (5, 17), (4, 5), (8, 8), (5, 7)]

    if all(x ** y == pow(x, y) for x, y in tests):
        print("Passed")
    else:
        print("Failed")


if __name__ == '__main__':
    main()

