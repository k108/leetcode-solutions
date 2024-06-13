import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq = {}
        len_heap = 0
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
                len_heap += 1
        heap = []
        heapq.heapify(heap)
        for key in freq.keys():
            heapq.heappush(heap, (-freq[key], key))

        return [heapq.heappop(heap)[1] for _ in range(k)]
        
