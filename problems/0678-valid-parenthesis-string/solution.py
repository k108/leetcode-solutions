class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        Time Complexity : O(n)
        Space Complexity : O(1)
        '''

        '''
        Approach :
        Greedy Strategy :
        Keep track of the minimum and maximum number of open parentheses 
        that must be matched
        - If the character is '(', increment both min_open_par and max_open_par by 1
        - If the character is ')', decrement both min_open_par and max_open_par by 1
        - If the character is '*', decrement min_open_par by 1 and increment max_open_par by 1
        - If max_open_par<0, return False, since it means there are more closing parentheses 
        than opening ones
        - If min_open_par<0, reset it to 0 since we can't have negative open parentheses count
        - Finally if min_open_par == 0 return True else False 
        '''
        min_open_par, max_open_par = 0, 0
        for c in s:
            if c == '(':
                min_open_par += 1
                max_open_par += 1
            elif c == ')':
                min_open_par -= 1
                max_open_par -= 1
            else:
                min_open_par -= 1
                max_open_par += 1

            if max_open_par < 0:
                return False
            if min_open_par < 0:
                min_open_par = 0
        
        return min_open_par == 0 
