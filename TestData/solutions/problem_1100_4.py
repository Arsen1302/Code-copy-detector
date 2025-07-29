class Solution:
    def solution_1100_4(self, releaseTimes: List[int], keysPressed: str) -> str:
        x = {releaseTimes[0] : keysPressed[0]}
        for i in range(1,len(releaseTimes)):
            a = releaseTimes[i] - releaseTimes[i-1]
            if a in x:
                if x[a] < keysPressed[i]:
                    x[a] = keysPressed[i]
            else:
                x[a] = keysPressed[i]
        return x[max(x.keys())]