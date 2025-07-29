class Solution:
    def solution_1633_1(self, tasks: List[int], space: int) -> int:
        
        ans = 0
        hashset = {}
        n = len(tasks)
        
        for x in set(tasks):
            hashset[x] = 0
            
        i = 0
        while i <= n - 1:
            flag = ans - hashset[tasks[i]]
            if flag >= 0:
                ans += 1
                hashset[tasks[i]] = ans + space
                i += 1
            else:
                ans += -flag
        
        return ans