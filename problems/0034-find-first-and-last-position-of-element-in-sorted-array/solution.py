class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def get_first_occurence(nums, N, target):
            low=0
            high=N-1
            while(low<=high):
                mid = (low+high)//2
                guess = nums[mid]

                # either guess is the first element of array or
                # the element to the right is less than it 
                if (mid==0 or nums[mid-1]<target) and guess==target:
                    return mid
                elif guess<target:
                    low=mid+1
                else:
                    # if guess==target, but not the first occurence, 
                    # then go left
                    high=mid-1

            return -1


        def get_last_occurence(nums, N, target):
            low=0
            high=N-1
            while(low<=high):
                mid = (low+high)//2
                guess = nums[mid]

                # either guess is the last element of array or
                # the element to the left is greater than it 
                if (mid==N-1 or nums[mid+1]>target) and guess==target:
                    return mid
                elif guess>target:
                    high=mid-1
                else:
                    # if guess==target, but not the last occurence, 
                    # then go right
                    low=mid+1
                    
            return -1

        N = len(nums)
        return [get_first_occurence(nums, N, target), get_last_occurence(nums, N, target)]

        
