class TrieNode:
    def __init__(self):
        self.children = {}
        self.last = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def form(self, keys):
        for k in keys:
            self.insert(k)

    def insert(self, key):
        node = self.root
        for k in key:
            if k not in node.children:
                node.children[k] = TrieNode()
            node = node.children[k]
        node.last = True

    def suggest_rec(self, node, key):
        if node.last:
            print(key)

        for k, n in node.children.items():
            self.suggest_rec(n, key + k)

    def suggest(self, key):

        print(f"\nKey: {key}")

        node, found = self.root, True
        for k in key:
            if k not in node.children:
                found = False
                break
            node = node.children[k]

        if not found:
            return -1
        elif node.last and not node.children:
            return 0

        self.suggest_rec(node, key)


def main():

    words1 = ["deer", "dog", "deep", "deal", "done", "deez"]
    key1 = "de"

    words2 = ["hello", "hell", "cat", "help", "helps", "helping"]
    key2 = "hel"

    trie = Trie()
    trie.form(words1)
    trie.suggest(key1)

    trie = Trie()
    trie.form(words2)
    trie.suggest(key2)


if __name__ == '__main__':
    main()
