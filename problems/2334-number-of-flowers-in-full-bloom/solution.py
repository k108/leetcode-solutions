from collections import defaultdict

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        '''
        Time Complexity : O((n + m) * logn),
        We first create two arrays of length n, starts and ends, then sort them. 
        This costs O(n * log(n)).
        
        Next, we iterate over people and perform two binary searches at each iteration. 
        This costs O(m * log(n)).

        Space Complexity : O(n),
        starts and ends both have a size of n
        '''

        '''
        At any given time, the number of flowers we see is the number of flowers 
        that have already started blooming minus the amount of flowers have finished blooming.

        We can simply collect all start points in one array starts, sort it, 
        and then perform a binary search. We can do the exact same thing with 
        another array ends for all end points.

        Regarding the binary searches: when binary searching on starts, 
        we want to search for the rightmost insertion index. This is because 
        if a person arrives at the same time as a flower starts blooming, 
        we want to include this flower. 

        Note that a flower = [start, end] stops blooming at end + 1, not end. 
        There are two ways we can handle this. We can either binary search on end 
        for the leftmost insertion index (since we want to include all flowers with 
        end equal to the current time), or we can assemble ends using end + 1 for each flower
        '''

        starts = []
        ends = []

        for start, end in flowers:
            starts.append(start)
            ends.append(end + 1)
        
        starts.sort()
        ends.sort()

        ans = []

        for person in people:
            i = bisect_right(starts, person)
            j = bisect_right(ends, person)
            ans.append(i - j)

        return ans
