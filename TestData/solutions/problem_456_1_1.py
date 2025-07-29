class Solution:
    def solution_456_1_1(self,x):
        flag=0
        if x==1:
            return False
        for i in range(2,x):
            if x%i==0:
                flag=1
                break
        if flag==1:
            return False
        return True
        
    def solution_456_1_2(self, left: int, right: int) -> int:
        arr_dict={}
        lst=list(range(left,right+1))
        for i in lst:
            if i not in arr_dict:
                arr_dict[i]=bin(i).replace("0b","")
        arr=list(arr_dict.values())
        count=0
        for i in arr:
            if self.solution_456_1_1(i.count('1')):
                # print(i)
                count+=1
        return count