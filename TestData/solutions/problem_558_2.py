class Solution:
    def solution_558_2(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if not stations:
            if startFuel >= target:
                return 0
            else:
                return -1
        dp = [0] * (len(stations) + 1)
        dp[0] = startFuel
        # utilize index as stop number
        for i in range(len(stations)):
            for j in range(i,-1,-1):
                if dp[j] >= stations[i][0]:
                    dp[j+1] = max(dp[j+1], dp[j] + stations[i][1])
        for i in range(len(dp)):
            if dp[i] >= target:
                return i
        return -1