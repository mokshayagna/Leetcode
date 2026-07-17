class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        total_cost = 0
        curr_gas = 0
        start = 0
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            curr_gas = curr_gas + (gas[i] - cost[i])
            if curr_gas < 0:
                start = i+1
                curr_gas = 0
        # sum of gas available is not sufficient 
        if total_gas < total_cost:
            return -1
        return start