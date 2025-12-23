class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        Time Complexity : O(n*log(n))
        Space Complexity : O(1)
        '''
        '''
        Take one max weight person & one min weight person in the boat

        Try To first sit larger weight people, and if some space left then
        check for allowing smaller weight can fit in same boat, 
        allowing small weight people to sit in same boat help in reducing boat count
        '''
        people.sort()
        boats = 0

        left = 0
        right = len(people)-1

        while left<=right:
            # in case of left == right, although weight of a person is considered twice,
            # but it doesnt matter because only boat count is incremented
            weight = people[left] + people[right]
            if weight <= limit:
                left += 1
            boats += 1
            right -= 1

        return boats
