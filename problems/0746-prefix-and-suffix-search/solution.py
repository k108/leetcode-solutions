class WordFilter:
    '''
    Approach :
    We create 1 Map (prefix#suffix) => index;
    Later occurrences of the prefix + suffix combo will have its weight overwritten,
    so we can simply look up the dictionary and return the answer.
    '''

    def __init__(self, words: List[str]):
        '''
        Time Complexity : O(N × L²)
        Space Complexity : O(N × L²)
        '''
        # (prefix#suffix) => idx
        self.combo_to_index = {}

        for index, word in enumerate(words):
            prefix = ''
            for char in list(word):
                prefix += char
                suffix = ''
                for char in list(word[::-1]):
                    suffix += char
                    self.combo_to_index[prefix + '#' + suffix[::-1]] = index

    def f(self, prefix: str, suffix: str) -> int:
        '''
        Time Complexity : O(1)
        '''
        return self.combo_to_index.get(prefix + '#' + suffix, -1)
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
