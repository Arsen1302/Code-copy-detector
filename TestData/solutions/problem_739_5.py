class Solution:
    def solution_739_5(self, s: str) -> str:
        count = Counter(s)
        stack = deque()
        result = set()
        for i in s:
            if i in result: 
                count[i] -= 1
                continue

            while(stack and stack[-1] > i and count[stack[-1]] > 1):
                count[stack[-1]] -= 1
                result.remove(stack[-1])
                stack.pop()

            stack.append(i)
            result.add(i)

        return "".join(stack)