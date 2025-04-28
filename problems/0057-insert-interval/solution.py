class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        Time Complexity : O(n)
        Space Complexity : O(n)
        '''

        '''
        Since intervals array is sorted. we can use binary Search
        to find the correct position to insert interval.

        Merging the overlapping intervals while inserting the new interval
        can be done by comparing the end of the last interval 
        with the start of the new interval and vice versa.
        '''

        merged = []
        
        for interval in intervals:
            # if curr_interval_high < new_interval_low -> new_interval comes after
            if interval[1] < newInterval[0]:
                merged.append(interval)

            # if curr_interval_low > new_interval_high -> new_interval comes before 
            # we add the new interval and update it to the current one
            elif interval[0] > newInterval[1]:
                merged.append(newInterval)
                newInterval = interval

            # if curr_interval_high >= new_interval_low 
            # and curr_interval_low <= new_interval_high -> new_interval comes inside
            elif interval[1] >= newInterval[0] and interval[0] <= newInterval[1]:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]

        merged.append(newInterval)
        return merged
