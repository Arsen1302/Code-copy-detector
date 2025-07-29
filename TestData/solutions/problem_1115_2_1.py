class Solution:
    def solution_1115_2_1(self,code,k):
        res = []
        total = sum(code[1:k+1])
        res.append(total)
        i,j = 1,k+1
        while i<len(code):
            if j==len(code):
                j = 0
            total+=-code[i]+code[j]
            res.append(total)
            j+=1
            i+=1
        return res
    def solution_1115_2_2(self, code: List[int], k: int) -> List[int]:
        if k==0:
            return [0]*len(code)
        if k>0:
            return self.solution_1115_2_1(code,k)
        code = code[::-1]
        k=-1*k
        lst = self.solution_1115_2_1(code,k)
        return lst[::-1]