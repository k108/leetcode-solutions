class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        Time Complexity : n*log(n)
        Space Complexity : O(1)
        '''

        '''
        We can sort the array of balloons by their ending position.
        Then we make sure that while we take care of each balloon in order,
        we can shoot as many following balloons as possible.

        We should shoot as to the right as possible, because since balloons are sorted,
        this gives you the best chance to take down more balloons. Therefore the position
        should always be balloon[i][1] for the ith balloon.
        '''

        points.sort(key=lambda x: x[1])
        arrows = 1
        end = points[0][1]

        for start, finish in points[1:]:
            if start > end:
                arrows += 1
                end = finish

        return arrows
