class Solution:
    def solution_1065_5(self, s: str) -> str:
        stack = []
        mark = False
        for i in range(len(s)):
            if not mark and s[i] != "?":
                stack.append(s[i])

            elif mark and s[i] != "?":
                while stack[-1] == s[i]:
                    stack[-1] = chr((ord(stack[-1])+1-97)%26+97)
                stack.append(s[i])
                mark = False
                    
            elif s[i] == "?":
                if mark:
                    cur = stack[-1]
                    while stack[-1] == cur:
                        cur = chr((ord(stack[-1])+1-97)%26+97)
                else:
                    if stack:
                        cur = stack[-1]
                        while stack[-1] == cur:
                            cur = chr((ord(stack[-1])+1-97)%26+97)
                    else:
                        cur = "a"

                stack.append(cur)
                mark = True
            
        return "".join(stack)