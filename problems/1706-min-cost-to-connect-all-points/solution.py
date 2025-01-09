class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """

        Time Complexity : Min Heap Size = E and insertion E*log( E ) = E*log( V^2 ) = 2*E*log( V ) = E*log( V )

        Space Complexity : O(V+E), 
        Array to track visited vertices: Requires (O(V)) space to ensure each vertex is added to the MST only once 
        Array to maintain min-heap: Requires (O(E)) space 
        MST: Requires (O(V)) space to store the edges that make up the MST

        """
        n = len(points)
        
        if not points or n==1:
            return 0

        min_cost = 0

        def get_manhattan_distance(x_i, y_i, x_j, y_j):
            return abs(x_i - x_j) + abs(y_i - y_j)

        # create adjacency list
        adj = {}
        for i in range(n):
            for j in range(n):
                if i != j:
                    weight = get_manhattan_distance(points[i][0], points[i][1], points[j][0], points[j][1])
                    if i not in adj:
                        adj[i]=[]
                    if j not in adj:
                        adj[j]=[]

                    adj[i].append((j, weight))
                    adj[i].append((j, weight))

        # Initialize the heap by choosing a single node
        # (in this case 0) and pushing all its neighbors.
        minHeap = []
        for neighbor, weight in adj[0]:
            heapq.heappush(minHeap, [weight, 0, neighbor])

        mst = []
        visit = set()
        visit.add(0)
        while len(visit) < n:
            weight, n1, n2 = heapq.heappop(minHeap)
            if n2 in visit:
                continue
            min_cost+=weight
            mst.append([n1, n2])
            visit.add(n2)
            for neighbor, weight in adj[n2]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [weight, n2, neighbor])

        return min_cost
 
