class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        Time Complexity : O(n)
        Space Complexity : O(1)
        '''

        '''
        2 cases :
        - total_gas < total_cost, we can't complete the journey, so will return -1
        - current_gas+=gas[i]-cost[i], if we run out of fuel say at ith gas station. 
        All the gas station between ith and starting point are bad starting point as well.
        we can start trying at next gas station on the i + 1 station.
        '''
        start_point = 0
        current_gas = 0

        total_gas = 0
        total_cost = 0

        N = len(gas)

        for i in range(N):
            total_gas += gas[i]
            total_cost += cost[i]
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                start_point = i+1
                current_gas = 0
        
        return -1 if (total_gas < total_cost) else start_point  
