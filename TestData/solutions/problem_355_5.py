class Solution:
    def solution_355_5(self, flowerbed: List[int], n: int) -> bool:
#   Logic is simple at each index we check currnt position, prev and next position
#   if it contains "1" continue to next iteratinon
#   else increase count
#   if n is less than or equal to count , return True
        helper=[0]+flowerbed+[0]
        count=0
        for i in range(1,len(helper)-1):
            if helper[i]==1 or helper[i-1]==1 or helper[i+1]==1:
                continue
            else:
                count+=1
                helper[i]=1
        return count>=n