class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l_s1 = len(s1)
        l_s2 = len(s2)
        if l_s2<l_s1:
            return False

        window_freq = {}
        freq_target = {}
        for i in range(l_s1):
            if s1[i] not in freq_target:
                freq_target[s1[i]] = 1
            else:
                freq_target[s1[i]] += 1

            if s2[i] in s1:
                if s2[i] not in window_freq:
                    window_freq[s2[i]] = 1
                else:
                    window_freq[s2[i]] += 1

        if window_freq == freq_target:
            return True

        left,right=1, l_s1
        while right < l_s2:
            
            if s2[left-1] in freq_target:
                if s2[left-1] in window_freq:
                    window_freq[s2[left-1]] = max(0, window_freq[s2[left-1]]-1)
                    
            if s2[right] in freq_target:
                if s2[right] in window_freq:
                    window_freq[s2[right]] += 1
                else:
                    window_freq[s2[right]] = 1

            if window_freq == freq_target:
                return True

            left+=1
            right+=1

        return False






        
