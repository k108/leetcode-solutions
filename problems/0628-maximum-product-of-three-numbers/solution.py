class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        '''
        Time Complexity : O(N*log(K)), where K = 3 ~ O(N)
        Space Complexity : O(1)
        '''
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0] * a[1] * a[2], b[0] * b[1] * a[0])  
