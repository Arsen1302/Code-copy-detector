class Solution:
    def solution_1163_3_1(self, n: int) -> List[int]:
        ans, visited = [0] * (2 * n - 1), [False] * (n + 1)
        
        def solution_1163_3_2(idx: int) -> bool:
            nonlocal ans, visited, n
            if idx == len(ans):
                return True
            if ans[idx] != 0:
                return solution_1163_3_2(idx + 1)
            else:
                for num in range(n, 0, -1):
                    if visited[num]:
                        continue
                    visited[num], ans[idx] = True, num
                    if num == 1:
                        if solution_1163_3_2(idx + 1):
                            return True
                    elif idx + num < len(ans) and ans[idx + num] == 0:
                        ans[num + idx] = num
                        if solution_1163_3_2(idx + 1): 
                            return True
                        ans[idx + num] = 0
                    ans[idx], visited[num] = 0, False
            return False
        
        solution_1163_3_2(0)
        return ans