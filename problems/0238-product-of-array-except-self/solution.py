class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        suffix_products=[1]*N
        prefix_products=[1]*N
        answer=[1]*N
        for i in range(N):
            if i==0:
                suffix_products[i]=nums[i]
            else:
                suffix_products[i]=nums[i]*suffix_products[i-1]

            if i==0:
                prefix_products[N-1-i]=nums[N-1-i]
            else:
                prefix_products[N-1-i]=nums[N-1-i]*prefix_products[N-1-i+1]
        
        for i in range(N):
            if i==0:
                answer[i]=prefix_products[i+1]
            elif i==N-1:
                answer[i]=suffix_products[i-1]
            else:
                answer[i]=suffix_products[i-1] * prefix_products[i+1]
        
        return answer
        
