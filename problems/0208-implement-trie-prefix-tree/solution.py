class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Time Complexity : O(W*L), where 
        W is the number of words, and 
        L is an average length of the word
        """
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                current_node.children[c] = TrieNode()
            current_node = current_node.children[c]
        current_node.end_of_word = True

    def search(self, word: str) -> bool:
        """
        Time Complexity : O(W*L), where 
        W is the number of words, and 
        L is an average length of the word
        """
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c]
        return current_node.end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        """
        Time Complexity : O(W*L), where 
        W is the number of words, and 
        L is an average length of the word
        """
        current_node = self.root
        for c in prefix:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
