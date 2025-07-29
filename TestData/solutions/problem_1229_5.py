class Solution:
    def solution_1229_5(self, s: str, knowledge: List[List[str]]) -> str:
        d= {}
        for i in knowledge:
            d[i[0]] = i[1]
        z = ''
        x = ''
        flag = False
        for i in s:
            if i == '(':
                flag = True
            elif i == ')':
                flag = False
                z += d.get(x,'?')
                x = ''
            elif flag:
                x += i
            else:
                z += i
        return z