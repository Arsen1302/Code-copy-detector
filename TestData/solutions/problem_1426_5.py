class Solution:
    def solution_1426_5(self, street: str) -> int:
        c=0
        ls=list(street)
        for i in range(len(ls)):
            if ls[i]=="H":
                if i > 0 and ls[i-1]== "B":
                    continue
                if i+1<len(ls) and ls[i+1]==".":
                    ls[i+1]="B"
                    c+=1
                elif ls[i-1]=="." and i-1>=0:
                    ls[i-1]="B"
                    c+=1
                else:
                    return -1
        return c