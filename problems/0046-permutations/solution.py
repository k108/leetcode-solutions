class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        Time Complexity : O(n! * n^2)
        Space Complexity : O(n! * n)
        ''' 

        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        result = []
        for p in perms:
            for i in range(len(p)+1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                result.append(p_copy)

        return result

        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)

            perms = new_perms
        return perms    
        
        
