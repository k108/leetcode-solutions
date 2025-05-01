class Solution:

    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        '''
        Time Complexity : O(logn+logn+n)=O(n)
        Space Complexity : O(1+1+n)=O(n)
        '''

        '''
        Since intervals array is sorted. we can use binary Search
        to find the correct position to insert interval.

        Merging the overlapping intervals while inserting the new interval
        can be done by comparing the end of the last interval 
        with the start of the new interval and vice versa.
        '''

        # binary search the index si such that all intervals below si
        # end before the start of new_interval
        si = bisect.bisect_left(intervals, new_interval[0], key=lambda x: x[1])

        # binary search the index ei such that all intervals above ei
        # start after the end of new_interval
        ei = bisect.bisect_right(intervals, new_interval[1], key=lambda x: x[0])

        # Merge all intervals between si and ei,
        # by finding the minimum start and maximum end points
        start = min(intervals[si][0], new_interval[0]) if si < len(intervals) else new_interval[0]
        end = max(intervals[ei - 1][1], new_interval[1]) if ei > 0 else new_interval[1]

        return intervals[:si] + [[start, end]] + intervals[ei:]
