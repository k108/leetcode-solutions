class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        '''
        Time Complexity: O(n + E log E)
        Space Complexity: O(n + E)
        '''
        '''
        Approach :
        For every pair of emails in the same account, draw an edge between those emails.
        The problem is about enumerating the connected components of this graph.
        '''
        
        visited_persons = set()
        # {'<email>':[<person_index>]}
        emails_person_index_map = defaultdict(list)
        result = []

        # Build graph {'<email>':[<person_index>]}
        # O(E)
        for person_index, account in enumerate(accounts):
            for email in account[1:]:
                emails_person_index_map[email].append(person_index)

        # DFS for traversing person_indexes
        # Perform DFS on each account in accounts list and
        # look up emails_person_index_map to tell us which accounts are linked to that
        # particular account via common emails.
        # This will make sure we visit each account only once.
        # This is a recursive process and we should collect all the emails that we encounter.
        # O(n + E)
        def dfs(person_index, emails_encountered):
            if person_index in visited_persons:
                return
            visited_persons.add(person_index)
            for email in accounts[person_index][1:]:
                emails_encountered.add(email)
                for neighbour in emails_person_index_map[email]:
                    dfs(neighbour, emails_encountered)

        for person_index, account in enumerate(accounts):
            if person_index in visited_persons:
                continue
            person_name, emails_encountered = account[0], set()
            dfs(person_index, emails_encountered)
            # O(E log E)
            result.append([person_name]+sorted(emails_encountered))
        
        return result


