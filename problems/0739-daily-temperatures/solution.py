class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        monotonic_dec_stack = []
        result = [0]*N

        for i in range(N):
            while monotonic_dec_stack and monotonic_dec_stack[-1][0]<temperatures[i]:
                # keep popping till we find greater than current
                prev_val, prev_index = monotonic_dec_stack.pop()
                result[prev_index] = i - prev_index
            
            monotonic_dec_stack.append((temperatures[i], i))

        return result




        

        
        
