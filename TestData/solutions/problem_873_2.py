class Solution:
    def solution_873_2(self, s: str) -> List[str]:
        t = s.split(' ')
        
        l = 0
        for i in t:
            if l < len(i):
                l = len(i)
        
        final = []
        i = 0
        for j in range(l):
            st = ''
            for word in t:
                if i < len(word) and word[i]:
                    st += word[i]
                else:
                    st = st + ' '
            
            while len(st) >= 0:
                if st[-1] == ' ':
                    st = st[:-1]
                else:
                    break
                    
            i += 1
            final.append(st)
        
        return final