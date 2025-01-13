class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}
        for i in range(0, n):
            adj[i] = []
            
        # s = src, d = dst, w = weight
        for edge, w in zip(edges, succProb):
            adj[edge[0]].append([edge[1], w])
            adj[edge[1]].append([edge[0], w])

        shortest = {}
        minHeap = [[1, start_node]]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue

            shortest[n1] = w1
            if n1 == end_node:
                return -1*w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [-1 * abs(w1) * abs(w2), n2])
        return 0

