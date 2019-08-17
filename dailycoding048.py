"""
This problem was asked by Google.

Given pre-order and in-order traversals of a binary tree,
write a function to reconstruct the tree.

solution

"""
class Node:

    def __init__(self, val):
        self.left = self.right = None
        self.val = val


def construct_tree(inorder, preorder):
    """Recursively constructs a binary tree from and inorder & predorder traversal
    """

    # base cases
    if not inorder or not preorder:
        return

    root = Node(preorder[0])
    if len(preorder) == 1:
        return root

    # construct the tree
    for i, node in enumerate(inorder):
        if node == root.val:
            root.left = construct_tree(inorder[:i], preorder[1:i+1])
            root.right = construct_tree(inorder[i+1:], preorder[i+1:])
    return root


def inorder_it(root):
    """Returns list of inorder traversal for testing
    """ 
    inorder, stack = [], []
    curr = root

    while stack or curr:
        if not curr:
            node = stack.pop()
            inorder.append(node.val)
            curr = node.right
        else:
            stack.append(curr)
            curr = curr.left

    return ''.join(inorder)

def preorder_it(root):
    """Returns list of preorder traversal for testing
    """
    preorder, stack = [], []
    stack.append(root)

    while stack:
        node = stack.pop()
        preorder.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return ''.join(preorder)


def run_tests(tests):
    result = True
    for t in tests:
        tree = construct_tree(*t)
        result &= (t[0] == inorder_it(tree) and t[1] == preorder_it(tree))
    return result


def main():

    tests = (
        ("dbeafcg", "abdecfg"),
        ("dbeacg", "abdecg")
    )

    if run_tests(tests):
        print("Passed")
    else:
        print("Failed")


if __name__ == '__main__':
    main()
        
