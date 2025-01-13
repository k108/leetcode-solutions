class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
            '''
            Time Complexity : E*log( V )
            Space Complexity : O( V+E )
            '''
            max_weight = -1
            adj = {}
            for i in range(1, n + 1):
                adj[i] = []
                
            # s = src, d = dst, w = weight
            for s, d, w in times:
                adj[s].append([d, w])

            shortest = {}
            minHeap = [[0, k]]
            while minHeap:
                w1, n1 = heapq.heappop(minHeap)
                if n1 in shortest:
                    continue
                shortest[n1] = w1
                max_weight = max(max_weight, w1)

                for n2, w2 in adj[n1]:
                    if n2 not in shortest:
                        heapq.heappush(minHeap, [w1 + w2, n2])

            if len(shortest)==n:
                return max_weight
            else:
                return -1

        
