s = [1,2,2]
index = 2
while len(s) < 100000:
    
    # what we append must be different from the last element
    # 1 -> first group only contains one number
    # 122 -> 1, 2 -> 3rd element is '2' ->  so we need to append 2, '1's -> 12211
    # 12211 -> 1, 2, 2 -> 3rd element is '1' -> so we need to append 1, '2' -> 122112

    # if last element 1 then val = 2, if last element 2 then val = 1
    val = 3 - s[-1]
    s.extend([val]*s[index])
    index += 1

class Solution:
    def magicalString(self, n: int) -> int:
        return s[:n].count(1)
        
