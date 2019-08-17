"""
This problem was asked by Google.

Implement an LRU (Least Recently Used) cache. It should be able to be
initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. If there are already n items in
the cache and we are adding a new item, then it should also remove
the least recently used item.
get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.

solution:
https://github.com/vineetjohn/daily-coding-problem/blob/master/
solutions/problem_052.py

https://www.geeksforgeeks.org/lru-cache-implementation/
"""

class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = self.prev = None


class LRU:
    def __init__(self, cache_lim):
        self.cache_lim = cache_lim
        self.cache = dict()
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node):
        prev_node = self.tail.prev
        node.next = self.tail
        node.prev = prev_node
        prev_node.next = node
        self.tail.prev = node

    def set(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.cache_lim:
            node_to_del = self.head.next
            self._remove(node_to_del)
            del self.cache[node_to_del.key]

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        return None


def main():

    lru = LRU(cache_lim=3)
    assert not lru.get("a"), print("Failed")
    lru.set("a", 1)
    assert lru.get("a") == 1, print("Failed")
    lru.set("b", 2)
    lru.set("c", 3)
    lru.set("d", 4)
    lru.set("e", 5)
    lru.set("a", 1)
    assert lru.get("a") == 1, print("Failed")
    assert not lru.get("b"), print("Failed")
    assert lru.get("e") == 5, print("Failed")
    assert not lru.get("c"), print("Failed")
    print("Passed")

if __name__ == '__main__':
    main()

