class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Time Complexity : O(n)
        Time Complexity : O(1)
        """
        # 'n' belongs to 1 to len(nums)+1
        # we use input array as hash set / memory
        # 1. we convert all the negative numbers as 0
        # 2. for each number, we take abs(number)-1 as index 
        # and multiply the number stored in it by -1
        # 3. if the number at index is 0 then as we cannot multiply it with -1,
        # we change it to -(len(nums)+1) i.e. out of bounds
        # 4. if all exist then we return N+1 positive integer

        N = len(nums)

        for i in range(N):
            if nums[i]<0:
                nums[i]=0

        for i in range(N):
            index = abs(nums[i])-1
            if index >=0 and index < N:
                if nums[index]==0:
                    nums[index]= -1*(N+1)
                elif nums[index]>0:
                    nums[index] *= -1

        for i in range(1, N+1):
            if nums[i-1]>=0:
                return i
        # if all exist then we return N+1 positive integer
        return N+1








        
