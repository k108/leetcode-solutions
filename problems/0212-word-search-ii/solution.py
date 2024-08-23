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


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Brute Force without Trie:
        Time Complexity : (w * m * n * 4 ^ m*n)
        Brute Force with Trie:
        Time Complexity : (m * n * 4 ^ m*n)
        """
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        result = set()

        def dfs(r, c, current_node, current_word):

            if r >= ROWS or r<0 or c<0 or c>=COLS or (r,c) in visited or board[r][c] not in current_node.children:
                return

            visited.add((r,c))

            current_node = current_node.children[board[r][c]]
            current_word += board[r][c]
            if current_node.end_of_word:
                result.add(current_word)

            dfs(r+1, c, current_node, current_word)
            dfs(r-1, c, current_node, current_word)
            dfs(r, c+1, current_node, current_word)
            dfs(r, c-1, current_node, current_word)
            
            visited.remove((r, c)) #backtracking

            return result

        trie = Trie()
        for word in words:
            trie.insert(word = word)
            
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j,trie.root, "")
    
        return list(result)

