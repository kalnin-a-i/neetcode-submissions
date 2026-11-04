class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        root = self.root

        for c in word:
            if not c in root:
                root[c] = {}
            root = root[c]
        
        root["*"] = "terminal"


    def search(self, word: str) -> bool:

        def dfs(root, string, i):
            # print(word)
            for j in range(i, len(string)):
                c = string[j]
                # print(c, root)
                if c == ".":
                    for other_c in root:
                        if other_c == "*":
                            continue
                        if dfs(root[other_c], string, j + 1):
                            return True
                    return False
                else:
                    if not c in root:
                        return False
                    root = root[c]
            return "*" in root

        return dfs(self.root, word, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)