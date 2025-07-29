class Solution:
    def solution_47_4_1(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        ### find start of the maximum sum subarray
        diff = [gas[i]-cost[i] for i in range(n)]
        return self.solution_47_4_2(diff)

    def solution_47_4_2(self, arr):
        maxSum, currSum = 0, 0
        maxStart, start = 0, 0
        for i in range(len(arr)):
            currSum += arr[i]
            if currSum > maxSum:
                ### the maximum sum is obtained when we start from index start
                maxStart = start
                maxSum = currSum
            if currSum < 0:
                ### reset the starting index
                start = i+1
                currSum = 0
        return start