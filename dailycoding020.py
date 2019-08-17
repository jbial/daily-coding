class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val


class List:
    def __init__(self):
        self.head = ListNode(0)

    def get_head(self):
        return self.head.next

    def get_tail(self):
        temp = self.head.next
        while temp.next:
            temp = temp.next
        return temp

    def get_node(self, index):
        temp = self.head.next
        for _ in range(index):
            temp = temp.next
        return temp

    def insert(self, val):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ListNode(val)

    def traverse(self):
        temp, liststr = self.head.next, ""
        while temp:
            liststr += f"{temp.val} -> " if temp.next else str(temp.val)
            temp = temp.next
        print(liststr)


def make_loop(head, count=1):
    while head.next:
        head = head.next
        count += 1
    return count, head


def find_intersection(list1, list2):

    # Find the length of list1 and make it cyclic
    count, end = make_loop(list1)
    end.next = list1

    # advance the runner ptr [count] times
    temp, runner = list2, list2
    for _ in range(count):
        if runner is None:
            return None
        runner = runner.next

    # Loop until equal
    while runner != temp:
        runner = runner.next
        temp = temp.next
    return temp


def main():

    list1 = List()
    list1.insert(1)
    list1.insert(2)
    list1.insert(3)
    list1.insert(4)

    list2 = List()
    list2.insert(5)
    list2.insert(6)
    list2.insert(7)
    list2.get_tail().next = list1.get_node(2)

    l1, l2 = list1.get_head(), list2.get_head()
    inter_node = find_intersection(l1, l2)
    print(inter_node.val if inter_node else -1)


if __name__ == '__main__':
    main()
