class Solution:
    def solution_669_4(self, num: List[int], k: int) -> List[int]:
        s=''
        new = []
        for i in num:
            s+=str(i)
        s = int(s) + k
        for i in str(s):
            new.append(int(i))
        return(new)