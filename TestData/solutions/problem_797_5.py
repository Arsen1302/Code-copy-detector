class Solution:
    def solution_797_5(self, arr: List[int]) -> bool:
        dit={}
        for i in range(len(arr)):
            if arr[i] in dit:
                dit[arr[i]]+=1
            else:
                dit[arr[i]]=1
        ans=[]
        for i, j in enumerate(dit):
            if dit[j] in ans:
                return False
            else:
                ans.append(dit[j])
        return True