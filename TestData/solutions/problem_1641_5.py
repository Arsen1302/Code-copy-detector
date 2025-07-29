class Solution:
    def solution_1641_5(self, s: str) -> str:
        res = [0] * (len(s) + 1)
        stack = []
        cur = 1
        for i in range(len(res)):
            if i == len(s) or s[i] == 'D':
                stack.append(i)
                if i < len(s):
                    continue
            else:
                res[i] = cur
                cur += 1
            while stack:
                res[stack.pop()] = cur
                cur += 1
        return ''.join(map(str,res))