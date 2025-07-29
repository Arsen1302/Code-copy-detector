class Solution:
    def solution_148_3_1(self, num: str) -> bool:
        #1 1 1=> 0 1 2 3
        #1 1 2=> 0 1 2 4
        #1 2 3=> 0 1 3 6 
        @cache
        def solution_148_3_2(i,j,k,l):
            if any([i>len(num),j>len(num),k>len(num),l>len(num)]):
                return False
            if any([num[i]=="0" and j-i!=1,num[j]=="0" and k-j!=1,num[k]=="0" and l-k!=1]):
                return False
            num1=int(num[i:j])
            num2=int(num[j:k])
            num3=int(num[k:l])
            if l==len(num):
                return num1+num2==num3
            o1=max(j-i,k-j)
            return num1+num2==num3 and (solution_148_3_2(j,k,l,l+o1) or solution_148_3_2(j,k,l,l+o1+1))
        
        maxPos=len(num)//2
        for i in range(1,maxPos+1,1):
            for j in range(1,maxPos+1,1):
                o1=max(i,j)
                if solution_148_3_2(0,i,i+j,i+j+o1) or solution_148_3_2(0,i,i+j,i+j+o1+1):
                    return True
        return False