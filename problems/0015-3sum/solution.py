class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        for i in range(len(nums)-2):
            first = nums[i]
            j = len(nums)-1
            k=i+1
            while k<j:
                potential_sum = nums[i]+nums[j]+nums[k]
                if potential_sum>0:
                    j-=1
                elif potential_sum<0:
                    k+=1
                else:
                    triplets.add((nums[i],nums[j],nums[k]))
                    j-=1
                    k+=1
        return triplets
        
