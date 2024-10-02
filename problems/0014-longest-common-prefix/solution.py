class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        N = len(strs)
        word = strs[0]
        L = len(word)
        count = 0
        for i in range(L):
            for j in range(1,N):
                if len(strs[j])>i:
                    if strs[j][i]!=word[i]:
                        return word[0:count]
                else:
                    return word[0:count]
            count += 1
        return word[0:count]
        

