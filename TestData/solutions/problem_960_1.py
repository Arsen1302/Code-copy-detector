class Solution:
    def solution_960_1(self, paths: List[List[str]]) -> str:
        lst=[]
        arr=[]
        for i in paths:
            lst.append(i[0])
            arr.append(i[1])
        ptr=set(lst)
        ptr2=set(arr)
        return list(ptr2-ptr)[0]