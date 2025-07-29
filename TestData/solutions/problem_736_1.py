class Solution:
    def solution_736_1(self, text: str, first: str, second: str) -> List[str]:
        ans, stack = [], []
        for w in text.split():
            if len(stack) > 1 and stack[-2] == first and stack[-1] == second:
                ans.append(w)
            stack.append(w)
        return ans