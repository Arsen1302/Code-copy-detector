class Solution:
    def solution_1399_4_1(self, sentence: str) -> int:
        sen = sentence.split()
        r, m = 0, 0
        _digits = re.compile('\d')
        
        def solution_1399_4_2(s):
            a, b, c = 0, 0, 0
            a = s.count('!')
            b = s.count(',') 
            c = s.count('.')
            
            if (a+b+c) == 0:
                return 1
            elif (a+b+c) == 1:
                if s[-1] in ['!',',','.']:
                    return 1
            return 0
        
        for s in sen:
            if not bool(_digits.search(s)):
                m = s.count('-')
                if m == 1:
                    a = s.index('-')
                    if a != 0 and a != len(s)-1 and s[a+1].isalpha():
                        r += solution_1399_4_2(s)
                elif m == 0:
                    r += solution_1399_4_2(s)
        return r