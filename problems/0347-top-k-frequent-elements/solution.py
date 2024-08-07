class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)

        if N==k:
            return nums

        counts = {}

        for num in nums:
            if num not in counts:
                counts[num]=0
            counts[num]+=1
        
        freq = [[] for _ in range(N+1)]

        for key,count in counts.items():
            freq[count].append(key) 

        ans = []
        count = 0
        for i in freq[::-1]:
            for j in i:
                ans.append(j)
                count+=1

                if count == k:
                    return ans



        
