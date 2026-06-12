class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    # Trie. time: O(n) for addWord, O(n) for search. space: O(t + n)
    # Where n is the length of the string and t is the total number of TrieNodes created in the Trie.
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
            for i, c in enumerate(word):
                if not cur.children:
                    return False
                if c == '.':
                    return any(inner_search(word[i+1:], child) for child in cur.children.values())
                if c not in cur.children:
                    return False
                cur = cur.children[c]
            return cur.word
        return inner_search(word, self.root)
