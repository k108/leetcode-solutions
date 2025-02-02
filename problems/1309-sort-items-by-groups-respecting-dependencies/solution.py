from collections import defaultdict

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        '''
        Time Complexity : O(n+e+m), where n nodes, m groups and e edges

        Space Complexity : O(n+e+m), where n nodes, m groups and e edges
        '''

        ''' 
        Topological Sort Approach :
        1. Create items graph based on before_items
        2. Create groups graph based on elements belonging to group 
        and their before_items and their group
        3. Run Topological sort and get items ordering and groups ordering
        4. Iterate on items ordering and append per group in groups ordering
        '''

        def topological_sort(adj, n, indegree):
            '''
            Time Complexity : O(V+E)
            Time Complexity : O(V)
            '''

            # Queue to store vertices with indegree 0
            q = deque()

            # STEP 1 : Push nodes with indegree 0 to queue
            for i in range(n):
                if indegree[i] == 0:
                    q.append(i)

            result = []

            # STEP 2 : Iterate through the queue
            while q:
                node = q.popleft()
                result.append(node)
                # STEP 3 : Decrease indegree of adjacent vertices 
                # as the current node is in topological order
                for adjacent in adj[node]:
                    indegree[adjacent] -= 1
                    # STEP 4 : If indegree becomes 0, push it to the queue
                    if indegree[adjacent] == 0:
                        q.append(adjacent)

            # STEP 5 : Check for cycle
            if len(result) != n:
                print("Graph contains cycle!")
                return []

            return result


        # STEP 1: Create a new group for each item that belongs to no group. 
        for u in range(len(group)):
            if group[u] == -1:
                group[u] = m
                m+=1

        # STEP 2: Build directed graphs for items and groups.
        items_adj = defaultdict(list)
        items_indegree = [0] * n
        group_adj = defaultdict(list)
        groups_indegree = [0] * m
        for i in range(n):
            for prev in beforeItems[i]:
                items_adj[prev].append(i)
                items_indegree[i] += 1
                if group[i]!=group[prev]:
                    group_adj[group[prev]].append(group[i])
                    groups_indegree[group[i]]+=1

        # STEP 3: Find topological orders of items and groups.
        item_order = topological_sort(items_adj, n, items_indegree)
        group_order = topological_sort(group_adj, m, groups_indegree)
        if not item_order or not group_order: return []

        # STEP 4: Find order of items within each group.
        group_to_items_inorder = defaultdict(list)
        for item in item_order:
            group_to_items_inorder[group[item]].append(item)

        # STEP 5. Combine ordered groups.
        result = []
        for group in group_order:
            result += group_to_items_inorder[group]
    
        return result


        
