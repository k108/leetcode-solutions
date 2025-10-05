class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        If number of unique characters are the same 
        and number of unqiue pairs are the same, we can return true.
        '''
        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))
