class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        '''
        Time Complexity : O(E + V * E + Q) = O(V * E + Q), 

        The result[adjacent].update(result[node]) operation takes at most O(V)
        in the worst case (when all nodes are connected).

        Building graph: O(P) where P is prerequisites length
        Processing courses: O(V * E) where:
        V = number of courses
        E = number of prerequisites edges
        Answering queries: O(Q) where Q is queries length
        Total: O(V * E + Q)

        Space Complexity : O(E + V^2),

        Adjacency List: O(P)
        Queue: O(V)
        Prerequisites Map: O(V * E)
        Total: O(V * E)
        '''

        adj = defaultdict(list)
        indegree = [0] * numCourses
        topological_sort = defaultdict(set)

        for crs, pre in prerequisites:
            adj[crs].append(pre)
            indegree[pre] += 1
            

        def topological_sort(adj, n, indegree):
            '''
            Time Complexity : O(V+E)
            Time Complexity : O(V)
            '''

            # Queue to store vertices with indegree 0
            q = deque()
            for i in range(n):
                if indegree[i] == 0:
                    q.append(i)
            # result = []
            # Use a map to store all prerequisites for each course
            result = defaultdict(set)
            while q:
                node = q.popleft()
                # result.append(node)
                # Decrease indegree of adjacent vertices as the current node is in topological order
                for adjacent in adj[node]:
                    # For each course we process:
                    # Add it as a prerequisite to its dependent courses
                    result[adjacent].add(node)
                    # Pass down all its prerequisites
                    result[adjacent].update(result[node])
                    indegree[adjacent] -= 1
                    # If indegree becomes 0, push it to the queue
                    if indegree[adjacent] == 0:
                        q.append(adjacent)

            # Check for cycle
            if len(result) != n:
                print("Graph contains cycle!")
                return defaultdict(set)
            return result


        topo_sorted_results = topological_sort(adj, numCourses, indegree)

        return [q_crs in topo_sorted_results[q_pre] for q_crs, q_pre in queries]
