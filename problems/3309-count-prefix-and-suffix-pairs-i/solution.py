class PrefSuffTrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = 0

class PrefSuffTrie:

    def __init__(self):
        self.root = PrefSuffTrieNode()

    def insert(self, word: str) -> None:
        """
        Time Complexity : O(W*L), where 
        W is the number of words, and 
        L is an average length of the word
        """
        current_node = self.root
        for i in range(len(word)):
            prefix = word[i]
            suffix = word[len(word) - 1 - i]
            if (prefix, suffix) not in current_node.children:
                current_node.children[(prefix, suffix)] = PrefSuffTrieNode()
            current_node = current_node.children[(prefix, suffix)]
            current_node.end_of_word += 1

    def search(self, word: str) -> bool:
        """
        Time Complexity : O(W*L), where 
        W is the number of words, and 
        L is an average length of the word
        """
        current_node = self.root
        for i in range(len(word)):
            prefix = word[i]
            suffix = word[len(word) - 1 - i]
            if (prefix, suffix) not in current_node.children:
                return 0
            current_node = current_node.children[(prefix, suffix)]
        return current_node.end_of_word

class Solution:

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        '''
        Time Complexity : O(n * m), where m is the average string length.
        The insert operation takes O(m) time, and the starts_with operation also takes O(m) time
        Space Complexity : O(n * m)
        '''

        '''
        Hello
        olleH
        (H,o)
        (e,l)
        (l,l)
        (l,e)
        (o,H)

        ababa
        ababa
        (a,a)
        (b,b)
        (a,a)
        (b,b)
        (a,a)

        aba
        aba
        (a,a)
        (b,b)
        (a,a)

        We iterate from the back of the list of words, calculating how many previously
        processed words would have the current word as both prefix and suffix,
        then add the current word to the trie.

        The trie itself holds info about both prefixes and suffixes simultaneously,
        as we don't need them separately
        '''
        count = 0
        trie = PrefSuffTrie()

        for word in words[::-1]:
            count += trie.search(word)
            trie.insert(word)
          
        return count
