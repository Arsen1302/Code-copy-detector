class Solution:
    def solution_683_1(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i == 'a':stack.append(i)
            elif i=='b':
                if not stack:return False
                else:
                    if stack[-1]=='a':stack.pop()
                    else:return False
                    stack.append(i)
            else:
                if not stack:return False
                else:
                    if stack[-1]=='b':stack.pop()
                    else:return False

        return len(stack)==0