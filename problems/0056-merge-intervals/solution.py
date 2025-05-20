class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        Time Complexity : O(n log n)

        Space Complexity : O(log N) (or O(n))
        If we can sort intervals in place, we do not need more than constant additional space, although the sorting itself takes O(logn) space. Otherwise, we must allocate linear space to store a copy of intervals and sort that.
        '''
        '''
        Approach :
        All mergeable intervals must occur in a contiguous run, of the sorted list
        '''
        intervals = sorted(intervals, key=lambda e : (e[0], e[1]))

        merged = []
        for interval in intervals:
            # If the current interval is the first element or
            # If the current interval begins after the previous interval ends, 
            # then they do not overlap and we can append the current interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # merge them by updating the end of the previous interval,
                # if it is less than the end of the current interval
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

# Test Cases :
# s = Solution()
# assert [[0, 1]] == s.merge([[0, 1]])
# assert [[0, 1], [2, 3]] == s.merge([[0, 1], [2, 3]])
# assert [[0, 3]] == s.merge([[0, 1], [1, 3]])
# assert [[0, 1]] == s.merge([[0, 1], [0, 1], [0, 1]])
# assert [[0, 5]] == s.merge([[1, 4], [0, 2], [3, 5]])
