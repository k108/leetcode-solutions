import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        '''
        Time Complexity : O(a + b + c)
        Space Complexity : O(1)
        '''
        '''
        Greedy Approach : To make the string as long as possible, we try to use the character 
        that appears most often without breaking the rule about three consecutive characters. 
        If using the most frequent character would cause three in a row, 
        we use the next most frequent character instead.
        '''
        ans = ''
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))

        while heap:
            count, c =heapq.heappop(heap)
            if ans[-2:] == c*2:
                count_bak = count
                c_bak = c
                if heap:
                    count, c = heapq.heappop(heap)
                else:
                    return ans
                heapq.heappush(heap, (count_bak, c_bak))
            count *= -1
            ans += c
            count -= 1
            if count > 0:
                heapq.heappush(heap, (-(count), c))
        return ans
