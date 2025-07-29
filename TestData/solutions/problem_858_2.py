class Solution:
    def solution_858_2(self, arr: List[int], start: int) -> bool:
        n=len(arr)
        visited=[0]*n
        lst=[start]
        visited[start]=1
        while lst:
            x=lst.pop(0)
            if arr[x]==0:
                return True
            if x+arr[x]<n and visited[x+arr[x]]==0:
                lst.append(x+arr[x])
                visited[x+arr[x]]=1
            if x-arr[x]>=0 and visited[x-arr[x]]==0:
                lst.append(x-arr[x])
                visited[x-arr[x]]=1
        return False