class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        """
        Time Complexity :
        The time complexity of the provided code is determined by several factors:

        Counting the rankings for each team involves iterating over all the votes and updating a list of size n, which is the number of teams. Each vote takes O(n) time to iterate, and this is done for all m votes. So, this part of the algorithm takes O(m * n) time.

        Sorting the teams according to their rank counts and in case of a tie, using alphabetic ordering. Python's sort function uses TimSort, which has a worst-case time complexity of O(n * log(n)). Since there are n teams, sorting them takes O(n * log(n)) time.

        Generating the final string involves creating a string from the sorted teams, which takes O(n) time.

        Combining these factors, the overall time complexity is O(m * n + n * log(n) + n). Since n * log(n) is likely to be the dominant term as n grows in comparison to n, we can approximate the time complexity as O(m * n + n * log(n)).

        Space Complexity :
        The space complexity of the code is determined by:

        The space used by the cnt dictionary, which contains a list of counters, of size n, for each distinct team. Since there are n teams, the total size of the cnt dictionary is O(n^2).

        The space used by the sorting function could be O(n) in the worst case for the internal working storage during the sort.

        Taking these into account, the overall space complexity of the algorithm is O(n^2).
        """
        num_teams = len(votes[0])
        vote_counts = {}
        """
        vote_counts = {
            'A': [1, 1, 2],
            'B': [0, 2, 2],
            'C': [3, 1, 0]
            }
        """
        for vote in votes:
            for index, val in enumerate(vote):
                if val not in vote_counts:
                    vote_counts[val] = [0]*num_teams
                vote_counts[val][index] += 1
        ranked_teams = sorted(votes[0], key = lambda team : (vote_counts[team], -ord(team)), reverse=True)
        return "".join(ranked_teams)

        
