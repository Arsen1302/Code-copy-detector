class Solution:
    def solution_1326_2(self, A):
        n = len(A)
        stack, res = [], [0] * n
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= A[i]:
                stack.pop()
                res[i] += 1
            if stack: res[i] += 1
            stack.append(A[i])
        return res