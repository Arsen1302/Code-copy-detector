class Solution:
    def solution_1100_2(self, releaseTimes: List[int], keysPressed: str) -> str:
        for i in range(len(releaseTimes)-1, 0, -1):
            releaseTimes[i] = releaseTimes[i] - releaseTimes[i-1]
        return max(zip(releaseTimes,list(keysPressed)))[1]