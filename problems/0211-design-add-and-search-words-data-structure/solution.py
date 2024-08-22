class TrieNode:

    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        current_node = self.root

        for c in word:
            if c not in current_node.children:
                current_node.children[c] = TrieNode()
            current_node = current_node.children[c]
        current_node.end_of_word = True
        

    def search(self, word: str) -> bool:
        current_node = self.root
        W_LEN = len(word)

        def dfs(node, i):
            if i == W_LEN:
                return node.end_of_word

            if word[i] == '.':
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True

            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)

            return False

        return dfs(current_node, 0)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
