class Solution:
    def solution_903_2(self, num: int) -> List[int]:
		# Using Sort
        lis=[]  # lis in the format of [divisor1,divisor2,difference of divisor] Note** product of divisor=dividend
        for i in range(1,int(sqrt(num+1))+1):
            if (num+1)%i==0:
                lis.append((i,(num+1)//i,((num+1)//i)-i))
        
        for i in range(1,int(sqrt(num+2))+1):
            if (num+2)%i==0:
                lis.append((i,(num+2)//i,((num+2)//i)-i))
		lis=sorted(lis,key=lambda x:x[2])
        #print(lis)
        return [lis[0][0],lis[0][1]]