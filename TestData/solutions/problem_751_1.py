class Solution:
    operands = {"!", "&amp;", "|", "t", "f"}
    values = {"t", "f"}

    def solution_751_1(self, expression: str) -> bool:
        stack = []
        for c in expression:
            if c == ")":
                val = stack.pop()
                args = set()
                while val in Solution.values:
                    args.add(val)
                    val = stack.pop()
                if val == "!":
                    stack.append("f" if "t" in args else "t")
                elif val == "&amp;":
                    stack.append("f" if "f" in args else "t")
                elif val == "|":
                    stack.append("t" if "t" in args else "f")
            elif c in Solution.operands:
                stack.append(c)
        return stack[0] == "t"