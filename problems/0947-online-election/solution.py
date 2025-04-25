class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leading = []
        self.times = []
        votes_count = defaultdict(int)
        max_votes = 0
        for idx, p in enumerate(persons):
            votes_count[p] += 1
            if votes_count[p] >= max_votes:
                max_votes = votes_count[p]
                self.leading.append(p)
                self.times.append(times[idx])

    def q(self, t: int) -> int:
        idx = bisect.bisect_right(self.times, t)-1
        return self.leading[idx]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
