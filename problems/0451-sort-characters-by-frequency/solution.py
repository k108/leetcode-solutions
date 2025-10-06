class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        result = []
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        max_heap=[]
        for char, count in freq.items():
            heapq.heappush(max_heap, (-count, char))

        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char*(-count))

        return ''.join(result)
