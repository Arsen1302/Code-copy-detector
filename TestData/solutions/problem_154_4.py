class Solution:
    def solution_154_4(self, s: str) -> str:
        n, stack, dic = len(s), [], {}
        for i in range(n): dic[s[i]] = [0,i]
        
        for i in range(n):
            currChar = s[i]
            if dic[currChar][0]: continue
            while stack and stack[-1] > currChar and dic[stack[-1]][1] > i: dic[stack.pop()][0] = 0
            stack.append(currChar)
            dic[currChar][0] = 1
        return ''.join(stack)