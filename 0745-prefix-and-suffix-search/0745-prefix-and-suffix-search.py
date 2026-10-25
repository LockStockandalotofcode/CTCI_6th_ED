class TrieNode:
    def __init__(self):
        self.children = {}
        self.weight = -1

class WordFilter:
    def __init__(self, words: list[str]):
        self.root = TrieNode()
        for word_index, word in enumerate(words):
            word_len = len(word)
            # generate all suffix combinations, and populate trie with it
            for i in range(word_len + 1):
                to_insert = word[i:] + "#" + word

                # now simply insert into trie, character by character
                curr = self.root
                for char in to_insert:
                    if char not in curr.children:
                        curr.children[char] = TrieNode()
                    curr = curr.children[char]
                    curr.weight = word_index
                    # every node is updated with its weightmarker as index of latest word
                    # even when theres common prefixes for multiple words

    def f(self, pref: str, suff: str) -> int:
        query = suff + "#" + pref

        curr = self.root
        for char in query:
            if char not in curr.children:
                return -1
            curr = curr.children[char]

        return curr.weight


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)