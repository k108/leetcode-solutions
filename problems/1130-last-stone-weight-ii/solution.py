class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        return self.approach_7(stones)

    def approach_7(self, stones: List[int]) -> int:
        '''
        Time Complexity : O(N * total_sum)
        Space Complexity : O(total_sum)
        '''
        '''
        Approach : Difference-based Dynamic Programming using a set

        Recurrence Relation :

        State Definition :
        dp = set of all achievable differences
        after processing the current prefix of stones
        unq = {stones[0]}
        means:
        After processing the first stone, the only possible difference is stones[0].

        Base Case :
        dp = {stones[0]}
        (Equivalent to starting with {0} and processing the first stone.)

        Recurrence :
        For each stone s:
        dp_new = { |d + s|, |d − s|  for all d ∈ dp }

        tmp.add(abs(u + s))
        tmp.add(abs(u - s))

        Intuition :
        At any point 'd' represents the difference between two piles
        Adding a new stone s can:
        increase the difference -> d + s
        reduce / cancel part of the difference -> |d − s|
        We keep all reachable differences, and the smallest one at the end is optimal.

        Boundary Condition :
        Differences are always non-negative
        Maximum difference ≤ total sum of stones
        Set size is bounded by O(S)
        '''
        unique_differences = {stones[0]}

        for s in stones[1:]:
            tmp = set()
            for ud in unique_differences:
                tmp.add(abs(ud + s))
                tmp.add(abs(ud - s))

            unique_differences = tmp

        return min(unique_differences)

    def approach_7(self, stones: List[int]) -> int:
        '''
        Time Complexity : O(N * total_sum)
        Space Complexity : O(total_sum)
        '''
        '''
        Approach : Set-based difference DP

        Track all possible differences after each stone using:

        x + stone

        |x − stone|

        Return the smallest achievable difference.
        '''
        '''
        Recurrence Relation :

        State Definition :
        dp = set of all achievable differences

        Base Case :
        dp = {0}

        Recurrence :
        For each stone w:
        dp = { x + w, |x − w| | x ∈ dp }

        Intuition :
        Each stone can either:
        increase the difference, or
        cancel part of the existing difference
        This directly models the stone-smashing process.

        Boundary Condition :
        Differences are bounded by S
        Answer is min(dp)
        '''
        dp = {0}
        for stone in stones:
            dp = {stone + x for x in dp} | {abs(stone - x) for x in dp}
        return min(dp)

    def approach_6(self, stones: List[int]) -> int:
        '''
        Time Complexity : O(N * total_sum)
        Space Complexity : O(total_sum)
        '''
        '''
        Approach:
        Set-based subset sum DP / State-compression DP using sets

        All cases of "cancellation of rocks" can be expressed by two knapsacks.
        And the last stone value equals to the difference of these two knapsacks.
        It needs to be noticed that the opposite proposition is wrong.

        We use dp to record the achievable sum of the smaller group.
        dp[x] = 1 means the sum x is possible.

        Track all possible subset sums using a set.
        Compute min(|total_sum − 2*s|) over all achievable s.
        '''
        '''
        Recurrence Relation :

        State Definition :
        dp = set of all achievable subset sums

        Base Case :
        dp = {0}

        Recurrence :
        For each stone w:
        dp = dp ∪ { x + w | x ∈ dp }

        Intuition :
        Instead of a boolean DP table, directly track reachable sums.

        Boundary Condition :
        dp size ≤ S
        Final answer: min |S − 2*x|
        '''
        dp = {0}
        total_sum = sum(stones)
        for stone in stones:
            dp |= {stone + i for i in dp}
        return min(abs(total_sum - i - i) for i in dp)

    def approach_5(self, stones: List[int]) -> int:
        '''
        Time Complexity : O(N * total_sum)
        Space Complexity : O(total_sum)
        '''
        '''
        Approach : Iterative 1D-DP
        Bottom-up 1D DP (space-optimized knapsack)

        Compress DP from 2D → 1D by iterating backward.
        '''
        '''
        Recurrence Relation :

        State Definition :
        dp[j] = true if some subset forms sum j

        Base Case :
        dp[0] = true

        Recurrence :
        dp[j] = dp[j] OR dp[j − stone]
        (iterate j backward)

        Intuition :
        Same as 2D knapsack, but previous row is enough.
        Backward iteration avoids reuse of same stone.

        Boundary Condition :
        j iterates from S down to stone
        Scan j ≤ S/2 for result
        '''
        total_sum = sum(stones)
        dp = [False] * (total_sum + 1)
        dp[0] = True

        for stone in stones:
            for j in range(total_sum, stone - 1, -1):
                dp[j] = dp[j] or dp[j - stone]

        for s in range(total_sum // 2, -1, -1):
            if dp[s]:
                return total_sum - 2 * s

    def approach_4(self, stones: List[int]) -> int:
        '''
        Time Complexity : O(N * total_sum)
        Space Complexity : O(N * total_sum)
        '''
        '''
        Approach : Iterative DP
        Bottom-up 2D DP (0/1 Knapsack – subset sum)

        Minimum subset sum difference problem

        Compute all achievable subset sums using first i stones.
        Find the subset sum s ≤ total_sum/2 closest to half.
        '''
        '''
        Partition an array into 2 subsets whose difference is minimal,
        S1 + S2  = S
        S1 - S2 = diff  

        => diff = S - 2 * S2  => minimize diff equals to maximize S2

        => Find the maximum of S2, range from 0 to S / 2

        dp[i][j]   = {true if some subset from 1st to j'th has a sum equal to sum i, false otherwise}
            i ranges from (sum of all elements) {1..n}
            j ranges from  {1..n}
        '''
        '''
        Recurrence Relation : 
        
        State Definition :
        dp[i][j] = true if a subset of first i stones
        can form sum j

        Base Case :
        dp[0][0] = true
        dp[0][j] = false   (j > 0)

        Recurrence :
        dp[i][j] =
            dp[i − 1][j] OR
            dp[i − 1][j − stones[i − 1]]   (if j ≥ stones[i − 1])

        Intuition :

        For each stone, we decide:
        include it in the subset, or
        exclude it

        Classic 0/1 knapsack.

        Boundary Condition :

        i ∈ [0, N]
        j ∈ [0, S]
        Final answer from j ≤ S/2
        '''
        N = len(stones)
        total_sum = sum(stones)

        dp = [[False] * (total_sum + 1) for _ in range(N + 1)]

        # Base case
        for i in range(N + 1):
            dp[i][0] = True

        # DP transition
        for i in range(1, N + 1):
            for j in range(total_sum + 1):
                if stones[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - stones[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        # Find closest sum to total_sum // 2
        for s in range(total_sum // 2, -1, -1):
            if dp[N][s]:
                return total_sum - 2 * s

    def approach_3(self, stones: List[int]) -> int:
        '''
        Time Complexity : O(N * S)
        Space Complexity : O(N * S)
        '''
        '''
        Approach : Memoization / Top-down DP (subset partition)
        Top-down DP for minimum subset sum difference

        Recursively assign stones into two subsets (s1, s2) and minimize |s1 − s2|.
        Memoization works because (i, s1) uniquely determines s2.
        '''
        '''
        Recurrence Relation :

        State Definition :
        f(i, s1) = minimum difference achievable
        after assigning first i stones,
        sum of subset1 = s1
        (subset2 sum = S − s1)

        Base Case :
        f(N, s1) = |(S − s1) − s1|

        Recurrence :
        f(i, s1) = min(
            f(i + 1, s1 + stones[i]),   // put stone in subset1
            f(i + 1, s1)                // put stone in subset2
        )

        Intuition :

        We partition stones into two subsets.
        At the end, we want their sums as close as possible.

        Boundary Condition :

        s1 ∈ [0, S]
        DP state count: N × S
        '''
        N = len(stones)
        dp = [[-1] * (3000 + 1) for _ in range(30 + 1)]

        def dfs(i, s_1, s_2):
            if i == N:
                return abs(s_1-s_2)

            if dp[i][s_1] != -1:
                return dp[i][s_1]
            
            dp[i][s_1] = min(dfs(i+1, s_1 + stones[i], s_2), dfs(i+1, s_1, s_2 + stones[i]))
            return dp[i][s_1]
        
        return dfs(0, 0, 0)

    def approach_2(self, stones: List[int]) -> int:
        '''
        Time Complexity : O(N * S)
        Space Complexity : O(N * S)
        '''
        '''
        Approach : DFS + Memoization / Top-down DP

        Recurrence Relation :

        State : f(i, d), minimum achievable final difference
        after processing first i stones,
        current difference = d

        Base case :
        f(N, d) = |d|; all stones are used; the remaining difference is the answer.

        Recurrence :
        f(i, d) = min(
            f(i + 1, d + stones[i]),
            f(i + 1, d - stones[i])
        )

        Intuition :

        Each stone can either:
        increase the current difference, or reduce it
        Try both choices and pick the minimum outcome.

        Boundary Condition :

        i ranges from 0 to N
        No pruning -> explores all 2^N possibilities
        '''
        N = len(stones)
        dp = [[-1] * (3000 + 1) for _ in range(30 + 1)]

        def dfs(i, difference):
            if i == N:
                if difference < 0:
                    return float('inf')
                else:
                    return difference
            if difference > 0 and dp[i][difference] != -1:
                return dp[i][difference]
            
            result = min(dfs(i+1, difference + stones[i]), dfs(i+1, difference - stones[i]))
            if difference > 0:
                dp[i][difference] = result
            return result
        
        return dfs(0, 0)

    def approach_1(self, stones: List[int]) -> int:
        '''
        Time Complexity : O(2^N)
        Space Complexity : O(N), recursion stack
        '''
        '''
        Approach : Brute-force DFS / Exhaustive search (± sign assignment)

        For every stone, choose + or - and compute the final difference. 
        Try all 2^N possibilities and take the minimum valid result.

        For every element we have 2 choices, whether to give it "+" sign or "-" sign,
        as we can either add that elemnt or subtract it.
        Then we find out by which path we get the minimum answer,
        as we want total sum to be as least as possible
        So once we cover all elements we check what is the sum:
        => if negative: not possible as remaining stone cannot have negative weight,
        so we return infinity
        => if positive: then we return whatever the curr_sum was, and then check
        from which sign we are getting minimum answer
        '''
        N = len(stones)

        def dfs(i, difference):
            if i == N:
                if difference < 0:
                    return float('inf')
                else:
                    return difference
            return min(dfs(i+1, difference + stones[i]), dfs(i+1, difference - stones[i]))
        
        return dfs(0, 0)
