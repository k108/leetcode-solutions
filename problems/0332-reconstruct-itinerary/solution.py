from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
        Iterative Hierholzer's Algorithm : Eulerian Path/Circuit algorithm
        Time Complexity : O(E log(E))
        Space Complexity : O(E), size of adj and call stack
        '''

        adj = defaultdict(list)
        # Sort tickets list in descending order so that we can pop last element 
        # instead of pop out first element which is costly operation
        tickets.sort(reverse=True)
            
        for src, dst in tickets:
            adj[src].append(dst)

        stack = ["JFK"]
        itinerary = []

        while stack:
            curr = stack[-1]
            if not adj[curr]:
                # If we reach to an airport from where 
                # we can't go further then add it to the result. 
                # This airport should be the last to go 
                # since we can't go anywhere from here. 
                # That's why we return the reverse of the result
                # After this backtrack to the top airport in the stack and 
                # continue to traverse it's children
                itinerary.append(stack.pop())
            else:
                # Start with JFK as starting airport and 
                # keep adding the next child to traverse 
                # for the last airport at the top of the stack.
                stack.append(adj[curr].pop())

        return itinerary[::-1]

