"""
This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree.
Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).

solution:
Recurse on the tree. If the current node is an operator, then recursively evaluate
the operator on the left and right child of the current node. Otherwise if the
current node value is a numeric type, then return the value.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def eval_tree(root):
    if root.val.isnumeric():
        return int(root.val)
    return eval(f"{eval_tree(root.left)} {root.val} {eval_tree(root.right)}")


def main():
    
    a = Node('3')
    b = Node('2')
    c = Node('4')
    d = Node('5')
    
    d = Node('+')
    d.left = a
    d.right = b

    e = Node('+')
    e.left = c
    e.right = d

    f = Node('*')
    f.left = e
    f.right = d

    tests = {
        a: 3,
        d: 5,
        e: 9,
        f: 45
    }

    if all(eval_tree(k) == tests[k] for k in tests):
        print("Passed")
    else:
        print("Failed")


if __name__ == '__main__':
    main()

