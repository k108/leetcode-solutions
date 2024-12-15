class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        visit = set()
        path = set()
        # topological_sort = []

        for crs, pre in prerequisites:
            if crs not in adjList:
                adjList[crs] = []
            if pre not in adjList:
                adjList[pre] = []
            adjList[crs].append(pre)

        def dfs(node):
            # # base case of crs with no pre
            # if adjList[node] == []:
            #     return True
            if node in path:
                return False
            if node in visit:
                return True

            visit.add(node)
            path.add(node)

            for neighbor in adjList[node]:
                if not dfs(neighbor):
                    return False

            # topological_sort.append(node)
            path.remove(node)

            return True

        for crs, pre in prerequisites:
            if not dfs(crs):
                return False

        return True

