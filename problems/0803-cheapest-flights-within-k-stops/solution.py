class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        Using Dijkstra's Algorithm

        Time Complexity : O(E*(k+1))
        Building the adjacency list: O(E)
        BFS traversal: O(E⋅(k+1))

        Space Complexity : O(E+V⋅(k+1))
        Adjacency list: O(E)
        Prices array: O(V)
        Queue: O(V⋅(k+1))
        '''
        prices = [float("inf")] * n
        prices[src] = 0
        adj = [[] for _ in range(n)]
        for u, v, cst in flights:
            adj[u].append([v, cst])

        '''
        Do we really need a priority queue for carrying out the algorithm? The answer for that is No because when we are storing everything in terms of a number of stops, the stops are increasing monotonically which means that the number of sops is increasing by 1 and when we pop an element out of the queue, we are always popping the element with a lesser number of stops first.

Replacing the priority queue with a simple queue will let us eliminate an extra log(N) of the complexity of insertion-deletion in a priority queue which would in turn make our algorithm a lot faster.
        '''
        q = deque([(0, src, 0)])
        while q:
            cst, node, stops = q.popleft()
            if stops > k:
                continue

            for nei, w in adj[node]:
                next_cst = cst + w
                if next_cst < prices[nei]:
                    # If a cheaper route to nei with next_stops stops is found
                    # then update and push to heap
                    prices[nei] = next_cst
                    q.append((next_cst, nei, stops + 1))

        return prices[dst] if prices[dst] != float("inf") else -1
