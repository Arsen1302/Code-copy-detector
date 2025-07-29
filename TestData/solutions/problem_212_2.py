class Solution:
    def solution_212_2(self, turnedOn):
        return ['{}:{}'.format(i,str(j).zfill(2)) for i in range(12) for j in range(60) if bin(i)[2:].count('1') + bin(j)[2:].count('1') == turnedOn]