class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        '''
        Time Complexity : O(n)
        Space Complexity : O(1)
        '''
        if bills[0] != 5:
            return False
        
        five_dollars = 0
        ten_dollars = 0

        for bill in bills:
            if bill == 5:
                five_dollars += 1
            elif bill == 10:
                if five_dollars >= 1:
                    five_dollars -= 1
                else:
                    return False
                ten_dollars += 1
            else:
                # Greedy : we rather save 5s than 10s
                if ten_dollars >= 1 and five_dollars >= 1:
                    ten_dollars -= 1
                    five_dollars -= 1
                elif five_dollars >= 3:
                    five_dollars -= 3
                else:
                    return False
 
        return True
        
