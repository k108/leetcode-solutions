from collections import defaultdict

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        '''
        Time Complexity : O(nlogn + mlogn)
        Space Complexity : O(n)
        '''
        '''
        Approach : Binary Search + Sweep Line
        
        Blooming flowers = started flowers - ended flowers
        '''

        start_times = []
        end_times = []

        for s, e in flowers:
            start_times.append(s)
            end_times.append(e)
        
        start_times = sorted(start_times)
        end_times = sorted(end_times)

        return [bisect_right(start_times, t) - bisect_left(end_times, t) for t in people]
