

def longest_path(string):
    max_len = 0
    levels = {-1: 0}
    for f in string.split("\n"):
        level = f.count("\t")
        levels[level] = len(f) - level + levels[level - 1]
        if '.' in f:
            max_len = max(max_len, levels[level] + level)
    return max_len


def main():

    string1 = "dir\n\tsubdir1\n\t\tsubsubdir2\n\t\t\tfile.ext\n\tsubdir2\n\t\tfile.ext"
    string2 = "dir\n\tfile.ext"
    string3 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    string4 = "dir\n\tsubdir1\n\t\tsubsubdir1\n\t\tfile.ext\n\t\tsubsubdir2\n\t\t\tfile.ext\n\tfile.ext"

    test1 = (string1, 31)
    test2 = (string2, 12)
    test3 = (string3, 32)
    test4 = (string4, 31)

    if (longest_path(test1[0]) == test1[1] and
        longest_path(test2[0]) == test2[1] and
        longest_path(test3[0]) == test3[1] and
            longest_path(test4[0]) == test4[1]):
        print("Passed")
    else:
        print("Failed")


if __name__ == '__main__':
    main()
