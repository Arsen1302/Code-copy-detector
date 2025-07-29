class Solution:
    def solution_1229_2(self, s: str, knowledge: List[List[str]]) -> str:
        K = { k[0] : k[1] for k in knowledge}
        stack = []
        for ch in s:
            if ch != ')':
                stack.append(ch)
            else:
                word = []
                while stack[-1] != '(':
                    word.append(stack.pop())
                stack.pop()
                stack.append(K.get(''.join(word[::-1]), '?'))
                
        return ''.join(stack)