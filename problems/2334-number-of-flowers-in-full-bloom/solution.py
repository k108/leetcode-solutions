from collections import defaultdict

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        '''
        Time Complexity : O(nlogn + mlogn)
        Space Complexity : O(n)
        '''
        '''
        Approach : TreeMap
        
        Stores key-value pairs in a sorted order (natural or custom) using a Red-Black Tree. 
        And it ensures O(log n) time for insertion, deletion and Seaching.
        '''

        diff = sortedcontainers.SortedDict({0: 0})
        for s, e in flowers:
            diff[s] = diff.get(s, 0) + 1
            diff[e + 1] =  diff.get(e + 1, 0) - 1
        
        count = list(accumulate(diff.values()))
        return [count[diff.bisect(t) - 1] for t in people]
