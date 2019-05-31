"""
This problem was asked by Quora.

Given a string, find the palindrome that can be made by inserting
the fewest number of characters as possible anywhere in the word. 
If there is more than one palindrome of minimum length that can be 
made, return the lexicographically earliest one (the first one alphabetically).

solution:

Use recursion to check the palindromes for three cases that consider
three important substrings: let S = S[1 ... N]
    case1) if S[1] == S[N], S[1] + palindrome(S[2 ... N-1]) + S[N]
    case2) S[1] + palindrome(S[2 ... N]) + S[1]
    case3) S[N] + palindrome(S[1 ... N-1]) + S[N]
Then, choose the palindrome with the minimum length, or the palindrome 
that comes lexicographically earlier if the lengths are the same.

This solution is exponential though, as the recursion tree includes
identical subproblems. Introduce a mem table to make the solution
faster
"""
def is_palinrome(string):
    """Check if string is palindrome (O(n) time)
    """
    return string == string[::-1]


def min_palindrome_rec(string, mem):
    """Recursively checks if the substrings are palindromes
    """
    # base case
    if is_palinrome(string):
        return string
    if string in mem:
        return mem[string]

    # case: first & last letters are the same
    if string[0] == string[-1]:
        mem[string[1:-1]] = min_palindrome_rec(string[1:-1], mem)
        return string[0] + mem[string[1:-1]] + string[-1]
    else:  # case: first letter != last letter

        mem[string[1:]] = min_palindrome_rec(string[1:], mem)
        mem[string[:-1]] = min_palindrome_rec(string[:-1], mem)
        pal1 = string[0] + mem[string[1:]] + string[0]
        pal2 = string[-1] + mem[string[:-1]] + string[-1]

        if len(pal1) < len(pal2):
            return pal1
        elif len(pal2) < len(pal1):
            return pal2
        return pal1 if pal1 < pal2 else pal2


def min_palindrome(string):
    return min_palindrome_rec(string, {}) 


def main():

    tests = {
        "race": "ecarace",
        "google": "elgoogle",
        "hello": "heolloeh",
        "algo": "algogla",
        "hannah": "hannah",
        "apple": "aelpplea"
    }

    if all(tests[k] == min_palindrome(k) for k in tests):
        print("Passed")
    else:
        print("Failed")

if __name__ == '__main__':
    main()
