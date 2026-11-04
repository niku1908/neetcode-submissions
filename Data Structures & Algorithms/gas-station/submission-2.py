class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        curr_gas, start_station = 0,0
        for i in range(len(cost)):
            curr_gas += gas[i]-cost[i]

            if curr_gas<0:
                start_station = i+1
                curr_gas = 0

        return start_station