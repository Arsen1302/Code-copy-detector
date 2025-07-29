class Solution:
    def solution_1229_3(self, s: str, knowledge: List[List[str]]) -> str:
        dic ={}
        for a,b in knowledge:
            dic[a] = b
        res, temp  = '', ''
        isopened = False
        for i in range(len(s)):
            if s[i] == '(':
                isopened = True
            elif s[i] == ')':
                key = temp
                if key in dic:
                    res = res + dic[key]
                else:
                    res = res + '?'
                temp = ''
                isopened = False
            elif  isopened == False:
                res = res + s[i]
            elif isopened == True:
                temp = temp + s[i]
        return res