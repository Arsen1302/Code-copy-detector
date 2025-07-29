class Solution:
    def solution_1241_3(self, obstacles: List[int]) -> int:
        ans = [0]*3 
        for i in reversed(range(len(obstacles) - 1)): 
            tmp = [inf]*3
            for k in range(3):
                if obstacles[i]-1 != k: 
                    tmp[k] = ans[k]
                    if obstacles[i]-1 != (k+1)%3: tmp[k] = min(tmp[k], 1 + ans[(k+1)%3])
                    if obstacles[i]-1 != (k+2)%3: tmp[k] = min(tmp[k], 1 + ans[(k+2)%3])
            ans = tmp
        return ans[1]