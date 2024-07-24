class Solution:
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {}
        adj_list = {i:[] for i in range(num_courses)}
        for a,b in prerequisites:
            if a in adj_list:
                adj_list[a].append(b)
            else:
                adj_list[a] = [b]
                
        visited = {}
        result = []
                
        def dfs(node):
            if node in visited:
                return visited[node]
                
            visited[node]=True
            
            for neighbor in adj_list[node]:
                if dfs(neighbor):
                    return True
            
            visited[node]=False
                
            result.append(node)
            
        
        for node in range(num_courses):
            if dfs(node):
                return []
                
        return result 
