class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        '''
        minimum number of times the string 'a' needs to be repeated 
        so that it contains the string 'b' as a substring

        For 'b' to be inside 'a', 'a' has to be repeated sufficient times
        such that it is at least as long as 'b' (or one more)
        '''
        repeats = -(-len(b)//len(a))

        for i in range(2):
            if b in (a * (repeats + i)):
                return repeats + i
    
        return -1   
