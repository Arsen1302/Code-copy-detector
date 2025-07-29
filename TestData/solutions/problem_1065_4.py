class Solution:
    def solution_1065_4(self, s: str) -> str:
        s= list(s)
        for i in range(0, len(s)):
            if s[i] == '?' and i == 0:

                try:
                    if s[i + 1] != 'a':
                        s[i] = 'a'
                        print('s:', s)
                    else:
                        s[i] = 'b'
                except:
                    return 'a'


            elif s[i] == '?' and i == len(s)-1:
                if s[i - 1] != 'a':
                    s[i] = 'a'
                else:
                    s[i] = 'b'

            else:
                if s[i] == '?':
                    if s[i - 1] != 'a' and s[i + 1] != 'a':
                        s[i] = 'a'
                    elif s[i - 1] != 'b' and s[i + 1] != 'b':
                        s[i] = 'b'

                    else:
                        s[i] = 'c'
                        
        return ''.join(s)