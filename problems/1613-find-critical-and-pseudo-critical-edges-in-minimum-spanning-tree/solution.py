class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        '''
        Time Complexity : O(ElogE+E^2 α(V)), Sorting the edges: O(ElogE) (done once)
        Each kruskalMST call:
        Iterates over E edges: O(Eα(V))
        Runs at most 2E times (once for each edge removed/forced)
        Total: O(E^2 α(V))

        Space Complexity :O(E+V)=O(E)
        '''

        import heapq

        class UnionFind:
            def __init__(self, n):
                self.par = {}
                self.rank = {}

                for i in range(0, n + 1):
                    self.par[i] = i
                    self.rank[i] = 0
            
            # Find parent of n, with path compression.
            def find(self, n):
                p = self.par[n]
                while p != self.par[p]:
                    self.par[p] = self.par[self.par[p]]
                    p = self.par[p]
                return p

            # Union by height / rank.
            # Return false if already connected, true otherwise.
            def union(self, n1, n2):
                p1, p2 = self.find(n1), self.find(n2)
                if p1 == p2:
                    return False
                
                if self.rank[p1] > self.rank[p2]:
                    self.par[p2] = p1
                elif self.rank[p1] < self.rank[p2]:
                    self.par[p1] = p2
                else:
                    self.par[p1] = p2
                    self.rank[p2] += 1
                return True

        # Given an list of edges of a connected undirected graph,
        # with nodes numbered from 1 to n,
        # return a list edges making up the minimum spanning tree.
        def minimumSpanningTree(edges, n, block, e):
            unionFind = UnionFind(n)
            # mst = []
            mst_weight = 0
            edges_used = 0  # Track number of edges added to MST

            #  If edge 'e' is forced, add it to the MST.
            if e!=-1:
                mst_weight += edges[e][2]  # Add the weight of the forced edge.
                unionFind.union(edges[e][0], edges[e][1])  # Union the vertices of the forced edge.       
                edges_used += 1
                
            for i in range(len(edges)):
                # Skip the edge if it's blocked.
                if i != block:
                    if not unionFind.union(edges[i][0], edges[i][1]):
                        continue
                    # mst.append([n1, n2])
                    mst_weight+=edges[i][2]
                    edges_used += 1

            return mst_weight if edges_used == n - 1 else float('inf')

        '''
        To find if one edge is critical, delete that edge and re-run the MST algorithm and
        see if the weight of the new MST increases.

        To find if one edge is non-critical (in any MST), include that edge to the accepted
        edge list and continue the MST algorithm, then see if the resulting MST has the same
        weight of the initial MST of the entire graph i.e. 
        Force the inclusion of the edge at the beginning of the MST. 
        If the MST weight remains the same, then this edge is pseudo-critical.
        '''

        '''
        Avoid Using a Heap (heapq):

        Sorting the edges once outside the function is O(E log E), whereas using a heap repeatedly O(E log E) per call slows it down.
        Instead, pass a pre-sorted list of edges to minimumSpanningTree, reducing sorting overhead.
        '''

        # Step 1: Sort edges by weight **once** (O(E log E))
        # Append index of each edge to keep track of their original position.
        for i in range(len(edges)):
            edges[i].append(i)
        edges.sort(key=lambda x: x[2])  # Sort by weight

        # Find the weight of the minimum spanning tree (MST) without blocking any edge.
        mst_weight = minimumSpanningTree(edges, n, -1, -1)

        # To store critical and pseudo-critical edges.
        critical_edges = []
        pseudo_critical_edges = []

        # Iterate through each edge to determine if it's critical or pseudo-critical.
        for i in range(len(edges)):
            # If excluding this edge results in a higher MST weight, it's critical.
            if minimumSpanningTree(edges, n, i, -1)>mst_weight:
                critical_edges.append(edges[i][3])
            # If including this edge results in the same MST weight, it's pseudo-critical.
            elif mst_weight==minimumSpanningTree(edges, n, -1, i):
                pseudo_critical_edges.append(edges[i][3])

    
        return [critical_edges, pseudo_critical_edges]
                
