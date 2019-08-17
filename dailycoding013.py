def update_window(string, k, start, key_map):
    while len(key_map.keys()) > k:
        key_map[string[start]] -= 1
        if key_map[string[start]] == 0:
            key_map.pop(string[start], None)
        start += 1
    return start


def longest_k_substr(string, k):
    counter = start = end = 0
    prev_len = max_start = max_end = 0
    key_map = {}
    for i in range(len(string)):

        # Check if char is in the map
        if string[i] not in key_map:
            key_map[string[i]] = 1
            counter += 1
        else:
            key_map[string[i]] += 1

        # Adjust the window bounds
        if counter > k:
            counter -= 1
            start = update_window(string, k, start, key_map)
        end += 1

        # Update return variable if length exceeds current max
        if len(string[start:end]) > prev_len:
            prev_len = len(string[start:end])
            max_start = start
            max_end = end

    return string[max_start:max_end]


def main():

    test1 = ("abcba", 2, "bcb")
    test2 = ("hello", 3, "hell")
    test3 = ("acceptance", 4, "accep")
    test4 = ("a", 1, "a")
    test5 = ("abcdefg", 7, "abcdefg")
    test6 = ("mississippi", 2, "ississi")
    test7 = ("banana", 3, "banana")

    if (longest_k_substr(*test1[:-1]) == test1[-1] and
        longest_k_substr(*test2[:-1]) == test2[-1] and
        longest_k_substr(*test3[:-1]) == test3[-1] and
        longest_k_substr(*test4[:-1]) == test4[-1] and
        longest_k_substr(*test5[:-1]) == test5[-1] and
        longest_k_substr(*test6[:-1]) == test6[-1] and
            longest_k_substr(*test7[:-1]) == test7[-1]):
        print("Passed")
    else:
        print("Failed")


if __name__ == '__main__':
    main()
