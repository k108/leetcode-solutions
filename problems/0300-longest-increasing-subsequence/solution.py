class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Time complexity: O(n * log(n))
        Space complexity: O(n)
        '''
        '''
        Greedy with Binary Search :-

        We create another subsequence of the same length, but ending with a smaller number x.

        Let’s say there are two increasing subsequences of the same length:

        A ends at 9
        B ends at 5

        Which one is better?

        Always B, because:

        any number > 9 is also > 5
        but many numbers > 5 are not > 9

        So B can be extended in more ways.

        This is why we only keep the smallest tail per length.

        Keep appending strictly increasing elements to lis arr.
        If we find an element < last greatest element of lis arr,
        we find it's appropriate place and insert it, i.e.
        find the index of the first element >= x, using binary search
        '''

        lis = []

        for num in nums:
            # Keep appending strictly increasing elements to lis
            if not lis or lis[-1] < num:
                lis.append(num)
            else:
                # Find the index of the first element >= x
                idx = bisect_left(lis, num)
                # Replace that number with x
                lis[idx] = num
        
        return len(lis)
