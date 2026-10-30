class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs_helper(index: int, curr: TrieNode) -> bool:
            for i in range(index, len(word)):
                char = word[i]
                if char == ".":
                    for child in curr.children.values():
                        if dfs_helper(i + 1, child):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    # check and move to the next character
                    curr = curr.children[char]

            return  curr.end_of_word
            
        return dfs_helper(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)