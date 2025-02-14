class UnionFind:
    '''
    Time Complexity : O(E*log(n)) -> O(E*1) -> O(E),
    Space Complexity : O(E)
    '''
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(1, n + 1):
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

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        '''
        Time Complexity : O(E log E) if we use sorting or 
        O(E) if we don't and only traverse edge list 

        Space Complexity : O(E), DSU's space
        '''
        '''
        Use disjoint set union data structure for both Alice and Bob.
        Always use Type 3 edges first, and connect the still isolated ones using other edges.
        '''
        removed_edge = 0
        dsu_alice = UnionFind(n)
        alice_edges = 0
        dsu_bob = UnionFind(n)
        bob_edges = 0

        # edges.sort(key= lambda x : x[0], reverse=True)

        for edge in edges:
            # check if this edge will actually  connect 2 components of alice & bob 
            # or its redundant
            if edge[0]==3:
                if (dsu_alice.union(edge[1], edge[2]) and dsu_bob.union(edge[1], edge[2])):
                    alice_edges+=1
                    bob_edges+=1
                else:
                    removed_edge+=1

        for edge in edges:
            # only alice
            if edge[0]==1:
                if dsu_alice.union(edge[1], edge[2]):
                    alice_edges+=1
                else:
                    removed_edge+=1
            # only bob
            elif edge[0]==2:
                if dsu_bob.union(edge[1], edge[2]):
                    bob_edges+=1
                else:
                    removed_edge+=1
        # both alice & bob should have n-1 edges to connect entire tree of alice & bob
        return removed_edge if (bob_edges == n-1 and alice_edges == n-1) else -1






        
