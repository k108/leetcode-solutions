class WordFilter:
    '''
    Approach :
    We create  2 Maps. One, Maps each word to its index.
    Another Maps (first_char, last_char) => list of words having that pattern;
    a coarse filter to reduce search space.
    Loop through words in reverse, it ensures that latest index is preserved.
    First check if there are any candidate words with matching first and last characters.
    Then for each candidate, verifies if the word actually matches the full prefix and suffix.
    Returns the stored index from map (which is the latest due to reverse traversal).
    '''

    def __init__(self, words: List[str]):
        '''
        Time Complexity : O(N)
        Space Complexity : O(N)
        '''
        # w => idx
        self.word_to_index = {}
        # (first_char, last_char) => [w1, w2,..]
        self.start_end_char_words = {}

        for i in range(len(words)-1,-1,-1):
            if (words[i][0],words[i][-1]) in self.start_end_char_words:
                self.start_end_char_words[(words[i][0],words[i][-1])].append(words[i])
            else:
                self.start_end_char_words[(words[i][0],words[i][-1])] = [words[i]]

            if words[i] not in self.word_to_index:
                    self.word_to_index[words[i]]=i

    def f(self, prefix: str, suffix: str) -> int:
        '''
        O(K × L)
        '''

        if (prefix[0],suffix[-1]) in self.start_end_char_words:
            candidates=self.start_end_char_words[(prefix[0],suffix[-1])]
            for candidate in candidates:
                # for each candidate, verify
                # if the word actually matches the full prefix and suffix
                if candidate[:len(prefix)]==prefix and candidate[len(candidate)-len(suffix):]==suffix:
                    return self.word_to_index[candidate]
        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
