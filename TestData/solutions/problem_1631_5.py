class Solution:
    def solution_1631_5(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        final=items1+items2
        final.sort(key=lambda i:(i[0]))
        for i in range(0,len(final)):
            for j in range(i+1,len(final)-1):
                if(final[i][0]==final[j][0]):
                    final[i][1]=final[i][1]+final[j][1]
                    del final[j] 
        if final[-1][0]==final[-2][0]:
            final[-2][1]=final[-2][1]+final[-1][1]
            del final[-1]
        return final