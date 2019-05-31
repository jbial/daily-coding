"""
This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring.
If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb".
The longest palindromic substring of "bananas" is "anana".

solution:
1) Use a recursive approach. The base case is if the string is empty
    or if it already a palindrome which checks in O(N) time. Otherwise try
    all possible starting and ending positions. There are N choose 2 possible
    starting and ending solutions excluding trivial solutions (choosing 
    individual characters as palindromes) and each function call does O(N) 
    in is_palindrome. Runs in O(N^3) time, constant space

2) Use an expanding window approach. Palindromes have mirror symmetry so expand
    a window about every pivot point in the string and keep track of the max
    palindrome. There are 2N-1 pivots since between chars and chars can be pivots
    in a palindrome, and expanding a window takes O(N), so runs in O(N^2) time,
    constant space.
"""
def is_palindrome(string):
    return string == string[::-1]


def palindromic_substr(string):
    """Recursive method **very slow**
    """
    if not string or is_palindrome(string):
        return string
    
    s1 = palindromic_substr(string[1:])
    s2 = palindromic_substr(string[:-1])

    return s1 if len(s1) >= len(s2) else s2


def expand_win(string, left, right):
    while left >= 0 and right < len(string) and (string[left] == string[right]):
        left -= 1
        right += 1
    return right - left - 1


def longest_pal_dp(string):
    """Expanding window approach
    """
    start, end = 0, 0
    for i in range(len(string)):
        # expand from between chars
        len1 = expand_win(string, i, i + 1)
        # expand about char
        len2 = expand_win(string, i, i)
        
        max_len = max(len1, len2)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    return string[start: end + 1]


def main():
    
    tests = {
        "aabcdcb": "bcdcb",
        "google": "goog",
        "banana": "anana",
        "apple": "pp",
        "a": "a",
        "racecar": "racecar"
    }

    if all(longest_pal_dp(k) == tests[k] for k in tests):
        print("Passed")
    else:
        print("Failed")


if __name__ == '__main__':
    main()
