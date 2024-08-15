class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = max(piles)
        def finish_bananas(k):
            num_hours = 0
            for pile in piles:
                num_hours += math.ceil(pile/k)
            return num_hours<=h


        def binary_search(piles, left, right, min_k):
            if left>right:
                return min_k
            middle = (left+right)//2
            can_finish_bananas = finish_bananas(middle)
            if can_finish_bananas:
                min_k = min(min_k, middle)
                right = middle - 1
                return binary_search(piles, left, right, min_k)
            else:
                left = middle + 1
                return binary_search(piles, left, right, min_k)

        return binary_search(piles, 1, min_k, min_k)
                
        
