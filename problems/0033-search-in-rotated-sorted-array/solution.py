class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        left = 0
        right = N-1

        while(left <= right):
            middle = (left+right)//2
            guess = nums[middle]
            
            print(guess)

            if guess == target:
                return middle

            elif nums[left]<=guess:
                # In left portion
                if target > guess or nums[left]>target:
                    # Look in right
                    left = middle+1
                else:
                    # Look in left
                    right = middle-1
            else:
                # In right portion
                if target < guess or nums[right]<target:
                    # Look in left
                    right = middle-1
                else:
                    # Look in right
                    left = middle+1
        return -1

