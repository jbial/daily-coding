
def min_construction_cost(arr):
    prev_color = total_cost = 0
    for i in range(len(arr)):
        min_cost = arr[i][0]
        for j in range(1, len(arr[i])):
            if arr[i][j] < min_cost and j != prev_color:
                min_cost = arr[i][j]
                prev_color = j
        total_cost += min_cost
    return total_cost


def main():

    arr1 = [[5, 8, 1, 9],
            [4, 6, 19, 0],
            [4, 8, 14, 4],
            [4, 1, 18, 3]]

    arr2 = [[5, 8, 1, 9],
            [4, 6, 1, 2],
            [4, 1, 14, 4],
            [4, 1, 18, 3]]
    print(min_construction_cost(arr2))


if __name__ == '__main__':
    main()
