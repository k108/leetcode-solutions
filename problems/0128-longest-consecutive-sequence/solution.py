class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecutive_map = {}
        for num in nums:
            if num - 1 in consecutive_map:
                consecutive_map[num-1]=num
            if num + 1 in consecutive_map:
                consecutive_map[num]=num+1
            if num not in consecutive_map:
                consecutive_map[num]=None
        lcs = 0
        for key in consecutive_map.keys():
            if consecutive_map[key]==None:
                counter = 0
                while key in consecutive_map:
                    key -= 1
                    counter+=1
                lcs = max(lcs, counter)

        return lcs



            
        
