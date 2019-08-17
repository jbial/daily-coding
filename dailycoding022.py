def segment_string_rec(word_set, string, memo):
    if string in word_set:
        return string
    if string in memo:
        return memo[string]
    for i in range(len(string)):
        prefix = string[0:i]
        if prefix in word_set:
            suffix = string[i:len(string)]
            seg_suffix = segment_string_rec(word_set, suffix, memo)
            if seg_suffix:
                memo[string] = prefix + " " + seg_suffix
                return prefix + " " + seg_suffix
    return None


def segment_string(word_set, string):
    return segment_string_rec(word_set, string, {}).split(" ")


def main():

    tests = (
        ({'quick', 'brown', 'the', 'fox'}, "thequickbrownfox"),
        ({'bed', 'bath', 'bedbath', 'and', 'beyond'}, "bedbathandbeyond"),
        ({'aaa', 'aaaa'}, "aaaaaaa"),
        ({'a', 'aa', 'aaa', 'b'}, "aaaaaaaaab"),
        ({'eat', 'so', 'thats', 'that', 'sounds', 'neat'}, "thatsoundsneat"),
        ({'hell', 'hello', 'good', 'sir'}, "hellogoodsir")
    )

    test_ans = (
        ['the', 'quick', 'brown', 'fox'],
        ['bed', 'bath', 'and', 'beyond'],
        ['aaa', 'aaaa'],
        ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b'],
        ['that', 'sounds', 'neat'],
        ['hello', 'good', 'sir']
    )

    if all([segment_string(*tests[i]) == test_ans[i] for i in range(6)]):
        print("Passed")
    else:
        print("Failed")


if __name__ == '__main__':
    main()
