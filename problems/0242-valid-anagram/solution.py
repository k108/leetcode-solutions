class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l_s, l_t = len(s), len(t)
        if l_s != l_t:
            return False

        freq_s={}
        freq_t={}

        for i in range(l_t):
            if s[i] in freq_s:
                freq_s[s[i]]+=1
            else:
                freq_s[s[i]]=1

            if t[i] in freq_t:
                freq_t[t[i]]+=1
            else:
                freq_t[t[i]]=1
            
        return freq_s==freq_t
        
