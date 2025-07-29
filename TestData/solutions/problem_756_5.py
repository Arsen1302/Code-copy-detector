class Solution:
    def solution_756_5(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans1=[]
        ans2=[]
        for i in arr2:
            c=arr1.count(i)
            for j in range(c):
                ans1.append(i)
        for i in arr1:
            if i not in arr2:
                ans2.append(i)
        ans2.sort()
        return ans1+ans2