class Solution:
    def solution_63_5(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                x, y = stack.pop(), stack.pop()
                match token:
                    case "/":
                        stack.append(int(y / x))
                    case "+":
                        stack.append(y + x)
                    case "-":
                        stack.append(y - x)
                    case "*":
                        stack.append(y * x)
        return stack[0]