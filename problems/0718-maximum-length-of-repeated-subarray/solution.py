class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        Time Complexity : O(m * n)
        Space Complexity : O(m * n)
        '''
        '''
        Let dp[i][j] be the longest common prefix of A[i:] and B[j:]. 
        Whenever A[i] == B[j], we know dp[i][j] = dp[i+1][j+1] + 1. 
        The answer is max(dp[i][j]) over all i, j.
        '''
        
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                # else:
                    # if we are looking for longest common sequence,
                    # then we do dp[i][j] = max(dp[i + 1][j], dp[i][j + 1]); here
                    # however, this problem is looking for subarray,
                    # since both character is not equal, which means we need to break it here
                    # hence, set dp[i][j] to 0

        return max(max(row) for row in dp)
