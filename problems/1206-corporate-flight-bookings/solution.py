class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        '''
        Time Complexity : O(n*log(n))
        Space Complexity : O(n)
        '''
        seats = defaultdict(int)
        for booking in bookings:
            seats[booking[0]-1] += booking[2]
            seats[booking[1]] -= booking[2]

        ans = [0]*n
        for i in range(n):
            ans[i] = ans[i-1] + seats[i]
        return ans
