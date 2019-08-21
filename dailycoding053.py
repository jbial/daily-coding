"""
This problem was asked by Apple.

Implement a queue using two stacks. Recall that a queue is a FIFO
(first-in, first-out) data structure with the following methods:
enqueue, which inserts an element into the queue, and dequeue, which removes it.

Solution:
Continually push elements to the first stack for the enqueue operation, and for the
dequeue operation, flip all elements in the stack onto the second stack to retrieve
the first in element. This works even when enqueuing new elements onto stack one.
"""

class Queue:

    def __init__(self):
        self.s1 = list()
        self.s2 = list()

    def enqueue(self, elem):
        self.s1.append(elem)

    def dequeue(self):
        if len(self.s2) == 0:
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
        return self.s2.pop()


def main():

    q = Queue()

    # add test elements
    for i in range(10):
        q.enqueue(i)

    # dequeue first 5 elements
    for i in range(5):
        assert q.dequeue() == i, print("Failed")

    # add three elements
    for i in range(3):
        q.enqueue(i + 3)

    # check remaining 5 elements are properly dequeued
    for i in range(5):
        assert q.dequeue() == i + 5, print("Failed")

    # check remaining elements dequeued are correct
    for i in range(3):
        assert q.dequeue() == i + 3, print("Failed")

    print("Passed")


if __name__ == '__main__':
    main()


