class Solution:
    def solution_1615_2(self, s: str, e: str) -> bool:
        dl = dr = 0 
        for ss, ee in zip(s, e): 
            if dl > 0 or dl < 0 and ss == 'R' or dr < 0 or dr > 0 and ss == 'L': return False 
            dl += int(ss == 'L') - int(ee == 'L')
            dr += int(ss == 'R') - int(ee == 'R')
        return dl == dr == 0