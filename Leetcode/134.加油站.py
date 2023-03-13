class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        location = 0
        total_sum = 0
        if sum(gas) < sum(cost):
            return -1
        for index in range(len(gas)):
            total_sum += gas[index] - cost[index]
            if total_sum < 0:
                location = index + 1
                total_sum = 0
        return location


if __name__ == '__main__':
    S = Solution()
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(S.canCompleteCircuit(gas, cost))
