class Solution:
    def solution_1041_2(self, s: str) -> str:
        stack = []
        for c in s: 
            if stack and ord(stack[-1]) ^ ord(c) == 32: stack.pop() #pop "bad"
            else: stack.append(c) #push "good"
        return "".join(stack)