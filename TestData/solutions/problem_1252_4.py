class Solution:
    def solution_1252_4(self, word: str) -> int:
        d = {}
        d['a'] = {'a', 'e'}
        d['e'] = {'e', 'i'}
        d['i'] = {'i', 'o'}
        d['o'] = {'o', 'u'}
        d['u'] = {'u'}
		
        res, stack = 0, []
        for c in word: 
            # If stack is empty, the first char must be 'a'
            if len(stack) == 0:
                if c == 'a':
                    stack.append(c)
                continue 
            
            # If stack is NOT empty,
            # input char should be the same or subsequent to the last char in stack
            # e.g., last char in stack is 'a', next char should be 'a' or 'e'
            # e.g., last char in stack is 'e', next char should be 'e' or 'i'
            # ...
            # e.g., last char in stack is 'u', next char should be 'u'
            if c in d[stack[-1]]:
                stack.append(c)
                # If the last char in stack is eventually 'u', 
                # then we have one beautiful substring as candidate, 
                # where we record and update max length of beautiful substring (res)
                if c == 'u':
                    res = max(res, len(stack))
            else:
                stack = [] if c != 'a' else ['a']
                
        return res