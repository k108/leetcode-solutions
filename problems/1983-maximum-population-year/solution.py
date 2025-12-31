class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        '''
        Time Complexity : O(n + range_of_years)
        Space Complexity : O(101)
        '''
        '''
        Line Sweep :
        Given a sorted list of ranges on an axis and find the smallest integer
        with the maximum number of overlapping ranges

        Bucket Sort
        '''
        population = defaultdict(int)
        
        # how many ranges starts / ends at this given year
        for birth_year, death_year in logs:
            population[birth_year] += 1
            population[death_year] -= 1
            
        curr_pop = max_pop = result = 0

        # prefix sum
        for year in sorted(population):
            curr_pop += population[year]
            if curr_pop > max_pop:
                max_pop = curr_pop
                result = year
        
        return result
