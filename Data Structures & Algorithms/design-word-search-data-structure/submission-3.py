class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def inner_search(word: str, cur: TrieNode) -> bool:
            if not word:
                return True
            for i, c in enumerate(word):
                if not cur.children:
                    return False
                if c == '.':
                    if i == len(word) - 1:
                        return any(node.word for node in cur.children.values())
                    return any(inner_search(word[i+1:], child) for child in cur.children.values())
                if c not in cur.children:
                    return False
                cur = cur.children[c]
            return cur.word
        return inner_search(word, self.root)
