class Solution:
    def solution_154_3(self, s: str) -> str:
        n, lastIdx, insideStack, stack = len(s), [0] * 26, [0] * 26, []               # insideStack: it will show the current status of the stack, which character is present inside the stack at any particular instance of the loop.
        getIdx = lambda c: ord(c) - ord('a')                                          # it will return the index 
        for i in range(n): lastIdx[getIdx(s[i])] = i                                  # store the last index of the each character
        
        for i in range(n):
            currChar = s[i]                                                           # curr Char acter 
            if insideStack[getIdx(currChar)]: continue                                # if current character inside our stack, skkiiip it..
                
            while stack and stack[-1] > currChar and lastIdx[getIdx(stack[-1])] > i:  # we got a smaller character, pop the greater ones out only if its instance is present at the right part of the array from i
                insideStack[getIdx(stack.pop())] = 0                                  # we popped So, its no more inside stack, mark it in insideStack that its no more inside stack
                
            stack.append(currChar)                                                    # add the currChar 
            insideStack[getIdx(currChar)] = 1                                         # mark that currChar is inside our stack
        return ''.join(stack)                                                         # return the stack as a string