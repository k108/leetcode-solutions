class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # crs -> pre mapping
        adj = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        visited = set()
        
        def dfs(crs):
            if crs in visited:
                return False
            # base case of crs with not pre
            if adj[crs] == []:
                return True

            visited.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)
            adj[crs] = []

            return True

        # To handle the case if graph in not connected
        # 1->2, 3->4
        for crs in range(numCourses):
            if not dfs(crs) : return False
    
        return True

