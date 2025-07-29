class Solution:
    def solution_111_3(self, s: str) -> int:
        ops = {
            '+': lambda x,y: x+y,
            '-': lambda x,y: x-y,
        }
        digits=set('0123456789')
        num=0
        op = '+'
        stack = []
        i = 0
        while i< len(s):
            if s[i] == '(':
                stack.append((num, op))
                num = 0
                op = '+'
            elif s[i] == ')':
                tmp = stack.pop()
                num = ops[tmp[1]](tmp[0], num)
                op = '+'
            elif s[i] in '+-':
                op = s[i]
            elif s[i] in digits:
                j = i
                while j< len(s) and s[j] in digits:
                    j+=1
                num = ops[op](num, int(s[i:j]))
                i = j -1
            else:
                print("what", s[i])
            i+=1
        return num