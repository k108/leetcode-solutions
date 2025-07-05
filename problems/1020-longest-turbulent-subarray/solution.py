class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        '''
        Time Complexity = O(n)

        Space Complexity = O(1)
        '''
        '''
        we only care about the comparisons between adjacent elements. 
        If the comparisons are represented by -1, 0, 1 (for <, =, >), 
        then we want the longest sequence of alternating 1, -1, 1, -1, ...
        (starting with either 1 or -1)

        We know when the next block ends: when it is the last two elements being compared, 
        or when the sequence isn't alternating.

        -1 * -1 = 1
        1 * 1 = 1
        +1 * -1 = -1
        '''
        N = len(arr)
        start_idx = 0
        ans = 1

        def compare(a, b):
            return (a > b) - (a < b)

        for i in range(1, N):
            sign = compare(arr[i-1], arr[i])
            
            if sign == 0:
                start_idx = i
            elif i == N-1 or sign * compare(arr[i], arr[i+1]) != -1:
                ans = max(ans, i - start_idx + 1)
                start_idx = i

        return  ans 
