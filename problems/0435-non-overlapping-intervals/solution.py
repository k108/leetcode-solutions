class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Time Complexity : O(n log n);
        O(n log n) + O(n)

        Space Complexity : O(log N) (or O(n));
        If we can sort intervals in place, we do not need more than constant additional space, although the sorting itself takes O(logn) space. Otherwise, we must allocate linear space to store a copy of intervals and sort that.
        '''
        '''
        Approach :
        All mergeable intervals must occur in a contiguous run, of the sorted list

        Invert the problem : find the maximum number of intervals that are non-overlapping.

        if earliest finished is not included, we can always replace the first interval in the set with it.
        {all intervals} - {max compatible intervals} = minimum deleted intervals
        '''
        counter = 0
        intervals.sort(key=lambda e: e[1])
        last_finish = intervals[0][1]

        for start, end in intervals[1:]:
            if last_finish > start:
                counter += 1
            else:
                last_finish = end
        
        return counter

# Test Cases :
# s = Solution()
# assert 0 == s.eraseOverlapIntervals([[0, 1]])
# assert 0 == s.eraseOverlapIntervals([[0, 1], [2, 3]])
# assert 0 == s.eraseOverlapIntervals([[0, 1], [1, 3]])
# assert 2 == s.eraseOverlapIntervals([[0, 1], [0, 1], [0, 1]])
# assert 1 == s.eraseOverlapIntervals([[1, 4], [0, 2], [3, 5]])
# assert 7 == s.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]])
