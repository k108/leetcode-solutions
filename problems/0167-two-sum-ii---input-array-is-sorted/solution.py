class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i < j:
            temp = numbers[i] + numbers[j]
            if temp < target:
                i+=1
            elif temp > target:
                j-=1
            else:
                return [i+1, j+1]

        
