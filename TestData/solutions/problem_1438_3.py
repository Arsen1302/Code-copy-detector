class Solution:
    def solution_1438_3(self, security: List[int], time: int) -> List[int]:
        result=[]
        left=[0]*len(security)
        right=[0]*len(security)
        for i in range(1,len(security)):
            if security[i]<security[i-1]:
                left[i]=left[i-1]+1
            elif security[i]==security[i-1]:
                left[i]=left[i-1]+1
                right[i]=right[i-1]+1
            else:
                right[i]=right[i-1]+1
        print(left,right)
        for i in range(time,len(security)-time):
            if left[i]>=time:
                if right[i+time]>=time:
                    result+=[i]
        return result