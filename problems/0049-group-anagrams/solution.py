class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for word in strs:
            temp_word = "".join(sorted(word))
            if temp_word in freq:
                freq[temp_word].append(word)
            else:
                freq[temp_word] = [word]
        return freq.values()
