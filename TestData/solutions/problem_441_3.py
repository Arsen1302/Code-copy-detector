class Solution:
    def solution_441_3(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        result, stack = [0]*l, deque()
        for i in range(l):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                result[index] = i-index
            stack.append(i)
        return result