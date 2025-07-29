class Solution:
    def solution_1236_5(self, logs: List[List[int]], k: int) -> List[int]:
        dct = {}
        ans = [0] * k
        for log in logs:
            if log[0] in dct:
                dct[log[0]].add(log[1])
            else:
                dct[log[0]] = {log[1]}
        
        for i in dct.values():
            ans[len(i)-1] = ans[len(i)-1] + 1

        return ans