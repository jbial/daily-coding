
def sort_by_start(times):
    return sorted(times, key=lambda time: time[0])


def min_rooms(times):
    sorted_times = sort_by_start(times)
    rooms = 0
    queue = []
    queue.append(sorted_times[0])
    for t in range(1, len(sorted_times)):
        while queue and queue[0][1] < sorted_times[t][0]:
            queue.pop(0)
        queue.append(sorted_times[t])
        rooms = max(rooms, len(queue))
    return rooms


def main():

    import numpy as np
    a = np.a
    times = [
        ([(0, 30), (40, 60), (70, 80)], 1),
        ([(30, 75), (0, 50), (60, 150)], 2),
        ([(0, 30), (10, 50), (20, 100)], 3),
        ([(0, 100), (10, 90), (20, 80)], 3)
    ]

    if all([min_rooms(t) == r for t, r in times]):
        print("Passed")
    else:
        print("Failed")


if __name__ == '__main__':
    main()
