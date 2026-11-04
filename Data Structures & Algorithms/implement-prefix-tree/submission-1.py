class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        root = self.root

        for c in word:
            if not c in root:
                root[c] = {}
            root = root[c]
        
        root["*"] = 'terminal'

    def search(self, word: str) -> bool:
        root = self.root
        for c in word:
            if not c in root:
                return False
            root = root[c]
        
        return '*' in root

    def startsWith(self, prefix: str) -> bool:
        root = self.root

        for c in prefix:
            if not c in root:
                return False
            root = root[c]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)