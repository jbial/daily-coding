"""
This problem was asked by Facebook.

Given an unordered list of flights taken by someone,
each represented as (origin, destination) pairs, and a starting airport,
compute the person's itinerary. If no such itinerary exists, return null.
If there are multiple possible itineraries, return the lexicographically
smallest one. All flights must be used in the itinerary.

For example, given the list of flights
[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting
airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')]
and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C']
even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However,
the first one is lexicographically smaller.

solution:

Use backtracking, im fucking sick of backtracking see:
https://www.dailycodingproblem.com/blog/an-introduction-to-backtracking/
"""
def get_itinerary(flights, start, curr_itin=[]):
    if not flights:
        return curr_itin + [start]

    updated_itin = None
    for i, (city_1, city_2) in enumerate(flights):
        if city_1 == start:
            sub_itin = get_itinerary(
                flights[:i] + flights[i + 1:],
                city_2, curr_itin + [city_1])
            if sub_itin:
                if not updated_itin or "".join(sub_itin) < "".join(updated_itin):
                    updated_itin = sub_itin
    return updated_itin


def main():
    tests = (
        ([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL'),
        ([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A'),
        ([('SFO', 'COM'), ('COM', 'YYZ')], 'COM')
    )
    ans = (
        ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'],
        ['A', 'B', 'C', 'A', 'C'],
        None
    )

    if all(get_itinerary(*t) == a for t, a in zip(tests, ans)):
        print("Passed")
    else:
        print("Failed")


if __name__ == '__main__':
    main()
