from collections import defaultdict

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        '''
        Time Complexity : O(n log n) + O(m log m);

        O(n) + O(n log n) + O(m log m) + O(n + m). 
        The dominant terms are O(n log n) and O(m log m).

        Space Complexity : O(n + m)
        '''

        '''
        At any given time, the number of flowers we see is the number of flowers 
        that have already started blooming minus the amount of flowers have finished blooming.

        Count the number of flowers blooming at specific times for a list of people.

        First separate the start and end times of all flower blooming periods, sorts them,
        and then use a sweep-line algorithm. By iterating through the sorted people's 
        arrival times, track the number of currently blooming flowers by incrementing
        counter for each start time and decrementing it for each end time encountered.
        '''

        starts = []
        ends = []

        for start, end in flowers:
            starts.append(start)
            ends.append(end)
        
        starts.sort()
        ends.sort()

        ans = {}
        i = j = curr = 0

        for p in sorted(people):
            while i < len(starts) and starts[i] <= p:
                curr += 1
                i += 1
            
            while j < len(ends) and ends[j] < p:
                curr -= 1
                j += 1
            
            ans[p] = curr
        
        return [ans[p] for p in people]
