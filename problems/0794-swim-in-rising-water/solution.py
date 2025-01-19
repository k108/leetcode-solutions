import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R=len(grid)
        C=len(grid[0])
        max_weight = 0
        
        def shortestPath(grid, n, src, max_weight):
            shortest = {}
            minHeap = [[0, src]]
            while minHeap:
                w1, n1 = heapq.heappop(minHeap)
                if n1 in shortest:
                    continue
                shortest[n1] = w1
                print(grid[n1[0]][n1[1]])
                max_weight=max(max_weight, grid[n1[0]][n1[1]])
                if n1[0]==R-1 and n1[1]==C-1:
                    return max_weight

                for n2 in [(n1[0]+1, n1[1]), (n1[0]-1, n1[1]), (n1[0], n1[1]+1), (n1[0], n1[1]-1)]:
                    if n2[0]>=0 and n2[0]<R and n2[1]>=0 and n2[1]<C and n2 not in shortest:
                        w2=grid[n2[0]][n2[1]]
                        heapq.heappush(minHeap, [w2, n2])
            return max_weight

        return shortestPath(grid, R*C, (0,0), max_weight)

        
