from collections import defaultdict

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        '''
        Time Complexity : O(n) + O(max_end) + O(m), since max_end = 10^9, this solution gives TLE
        Space Complexity : O(max_end), since max_end = 10^9, this solution takes too much memory

        So we apply coordinate compression,
        We don’t care about all the numbers between 0 and 10^9, 
        only the ones that actually appear in our problem

        Instead of allocating arrays up to the largest number, 
        we map all relevant numbers to a small continuous range starting from 0

        Time Complexity : O((n + m) log n), O((n + m) log(n + m)) for sorting + O(n + m),
        for processing
        Space Complexity : O(n + m)
        '''

        # Step 1 : Collect all unique coordinates
        coordinates = set()
        for s, e in flowers:
            coordinates.add(s)
            coordinates.add(e+1)
        for p in people:
            coordinates.add(p)

        # Step 2 : Sort the coordinates
        coordinates = sorted(coordinates)

        # Step 3 : Map each real coordinate to a compressed index
        index_map = {coord: idx for idx, coord in enumerate(coordinates)}

        # Step 4 : Replace all values with compressed indices
        
        flower_count = defaultdict(int)
        max_end = 0
        for flower in flowers:
            start, end = flower
            flower_count[index_map[start]] = flower_count[index_map[start]] + 1
            flower_count[index_map[end+1]] = flower_count[index_map[end+1]] - 1
            max_end = max(index_map[end+1], max_end)
        
        overlapped_blooms = 0
        for i in range(max_end+1):
            overlapped_blooms += flower_count[i]
            flower_count[i] = overlapped_blooms
        
        ans = []
        for person in people:
            ans.append(flower_count[index_map[person]])
        
        return ans
