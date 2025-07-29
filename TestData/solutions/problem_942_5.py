class Solution:
    def solution_942_5(self, text):
        END = '&amp;'
        START = ';'
        d = {
            '&amp;quot;': '"',
            '&amp;apos;': "'",
            '&amp;amp;': '&amp;',
            '&amp;gt;': '>',
            '&amp;lt;': '<',
            '&amp;frasl;': '/',
        }
        stack = []
        seen_start = False
        for ch in reversed(text):
            if ch == START:
                seen_start = True
            stack.append(ch)
            if ch == END and seen_start:
                # check for a match
                temp = []
                while stack[-1] != START:
                    temp.append(stack.pop())
                temp.append(stack.pop()) # the ;
                val = ''.join(temp)
                if val in d:
                    stack.append(d[val])
                else:
                    stack.append(val)
                seen_start = False
        return ''.join(reversed(stack))