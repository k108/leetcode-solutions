class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        m = 10
        freq = defaultdict(int)
        result = []

        for i in range(n - m + 1):
            dna_seq = s[i: i+m]
            freq[dna_seq] += 1
            if freq[dna_seq] == 2:
                result.append(dna_seq)

        return result
