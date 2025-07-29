class Solution:
    def solution_1460_3(self, title: str) -> str:
        s = list(title.split(' '))
        sfin = ''
        for  i in range(len(s)):
            if len(s[i])>=3:
                sfin += s[i][0].upper()
                for  j in range(1,len(s[i])):
                    if s[i][j].isupper():
                        sfin+=s[i][j].lower()
                    else:
                            sfin+=s[i][j]
                if i+1!=len(s):
                    sfin+=' '
            else:
               
                for  j in range(len(s[i])):
                    if s[i][j].isupper():
                        sfin +=s[i][j].lower()
                    else:
                        sfin+=s[i][j]
                if i+1!=len(s):
                    sfin+=' '
        return sfin