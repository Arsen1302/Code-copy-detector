class Solution:
    def solution_1691_2(self, n: int, queries: List[List[int]]) -> List[int]:
        a=bin(n)[2:]
        # print(a)
        a=a[::-1]
        arr=[1]
        p=1
        for i in range(len(a)):
            if(a[i]=="1"):
                p*=2**i
                arr.append(p)
        ans=[]
        print(arr)
        for q in queries:
            p=arr[q[1]+1]//arr[q[0]]
            ans.append(p%(10**9+7))
        return ans