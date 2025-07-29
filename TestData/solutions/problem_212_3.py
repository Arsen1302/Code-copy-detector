class Solution:
    def solution_212_3(self, num: int) -> List[str]:
        res=[]
        for hour in range(12):
            for minutes in range(60):
                if bin(hour)[2:].count('1')+bin(minutes)[2:].count('1') ==num:
                        y= '{}:{}'.format(hour,str(minutes).zfill(2))
                        res.append(y)
        return res