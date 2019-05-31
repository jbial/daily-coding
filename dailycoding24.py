class LockTreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.val = val
        self.is_locked = False
        self.num_locked_children = 0

    def _can_lock_or_unlock(self):
        if self.num_locked_children > 0:
            return False

        # Traverse all the parent nodes to check is_locked
        curr = self.parent
        while curr:
            if curr.is_locked:
                return False
            curr = curr.parent
        return True

    def is_locked(self):
        return self.is_locked

    def lock(self):
        if self._can_lock_or_unlock():

            # locking is successful
            self.is_locked = True

            curr = self.parent
            while curr:
                curr.num_locked_children += 1
                curr = curr.parent
            return True
        else:
            return False

    def unlock(self):
        if self._can_lock_or_unlock():

            # Unlock the node
            self.is_locked = False

            curr = self.parent
            while curr:
                curr.num_locked_children -= 1
                curr = curr.parent
            return True
        else:
            return False


def main():

    root = LockTreeNode(100)
    root.left = LockTreeNode(200, parent=root)
    root.right = LockTreeNode(5, parent=root)
    root.left.left = LockTreeNode(300, parent=root.left)
    root.left.right = LockTreeNode(150, parent=root.left)
    root.left.right.left = LockTreeNode(170, parent=root.left.right)
    root.left.right.right = LockTreeNode(130, parent=root.left.right)

    root.left.right.lock()
    print(f"Locking a locked branch: {root.left.right.right.lock()}")
    print(f"Unlocking locked node: {root.left.right.unlock()}")
    print(f"Locking after unlock: {root.left.right.right.lock()}")


if __name__ == '__main__':
    main()
