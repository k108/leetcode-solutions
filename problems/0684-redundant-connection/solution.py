class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
        parent = [i for i in range(n)]
        rank = [1]*n

        def find(node):
            res = node

            while res != parent[res]:
                # path compression
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        def union(node_1, node_2):
            parent_1, parent_2 = find(node_1), find(node_2)

            if parent_1 == parent_2:
                return 0
            
            if rank[parent_2] > rank[parent_1]:
                parent[parent_1] = parent_2
                rank[parent_2] += rank[parent_1]
            else:
                parent[parent_2] = parent_1
                rank[parent_1] += rank[parent_2]
            return 1

        for n1, n2 in edges:
            result = union(n1, n2)
            if result == 0:
                return [n1, n2]

