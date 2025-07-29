class Solution:
    def solution_111_2_1(self, sign, num, stack):
        if sign == "+":
            stack.append(num)
        if sign == "-":
            stack.append(-num)
        return stack

    def solution_111_2_2(self, i, s):
        stack, num, sign = [], 0, "+"
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == "+" or s[i] == "-":
                stack = self.solution_111_2_1(sign, num, stack)
                num, sign = 0, s[i]
            elif s[i] == "(":
                num, i = self.solution_111_2_2(i + 1, s)
            elif s[i] == ")":
                stack = self.solution_111_2_1(sign, num, stack)
                return sum(stack), i
            i += 1
        # print(num, sign)
        stack = self.solution_111_2_1(sign, num, stack)
        return sum(stack)

    def solution_111_2_3(self, s: str) -> int:
        return self.solution_111_2_2(0, s)