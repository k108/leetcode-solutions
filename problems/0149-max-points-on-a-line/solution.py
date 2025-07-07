class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        '''
        Time Complexity : O(n*2)
        Space Complexity : O(n)
        '''
        '''
        Approach :
        If a set of points all lie on the same line, then the slope between any two points 
        in that set will be the same. This is because the slope of a line is constant, 
        and any two points on that line will define the same slope.

        For points = [[1,1], [2,2], [3,3]]
        For p1 = [1,1], the slope with [2,2] and [3,3] is the same.
        So slopes[1.0] = 2
        Then ans = max(slopes[slope], ans) = max(2, 1) = 2
        But since we only counted 2 other points, and need to include p1 as well, 
        we return ans + 1 = 3

        Even in the worst case—like a "skewed lattice" where no three points are collinear, 
        any two points will still form a line. So the smallest possible number of collinear
        points is 2, which the return ans + 1 correctly gives when ans = 1
        '''

        # If we only have 1 point then any line passes through it, so we return 1
        # If we only have 2 point then a line is the shortest path through both, so we return 2
        N = len(points)
        if N < 3:
            return N

        # We make a special helper func for finding the slope so we do not divide by 0
        def find_slope(p1, p2):
            # unpack the points into (x, y) coordinate pairs
            x1, y1 = p1
            x2, y2 = p2
            # Find the denominator or change in x
            delta_x = x1 - x2
            # Vertical lines have infinite slope, but python will give a ZeroDivisionError
            # so we check if the denominator is 0, **before dividing**
            if delta_x == 0:
                return float('inf')
            # Now we can safely divide via `Slope = change in y / change in x`
            return (y1 - y2) / delta_x

        # at least one point (p1 itself) is always part of the line
        ans = 1
        for i, p1 in enumerate(points):
            # For each point, create a new counter map: slope -> count of slope occurrences
            slopes = {}
            # Now for fixed `p1`, consider all future `p2`
            # where we only look at future points to avoid double-counting
            for p2 in points[i + 1:]:
                slope = find_slope(p1, p2)
                # and add one for the respective count
                slopes[slope] = slopes.get(slope, 0) + 1
                # Note that we have to update `ans` inside this loop as `slope` changes every iteration
                ans = max(slopes[slope], ans)
        # Add one to account for the point itself (to have 1 line you need 2 points)
        return ans + 1

# Test Cases :
# s = Solution()
# assert 3 == s.maxPoints(points = [[1,1], [2,2], [3,3]])
