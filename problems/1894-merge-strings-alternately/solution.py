class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = len(word1)
        j = len(word2)
        k = 0
        ans = []

        while k<i and k<j:
            ans.append(word1[k])
            ans.append(word2[k])
            k+=1
        while k<i:
            ans.append(word1[k])
            k+=1
        while k<j:
            ans.append(word2[k])
            k+=1

        return ''.join(ans)    
