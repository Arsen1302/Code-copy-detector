class Solution:
    def solution_1310_3(self, dist: List[int], speed: List[int]) -> int:
        if 0 in set(dist):
            return 0
        ans=[]
        for i,el in enumerate(dist):
            t=math.ceil(el/speed[i])
            ans.append(t)
        ans.sort()
        count=0
        prev=0
        print(ans)
        for i in range(len(ans)):
            if prev==ans[i]:
                return count
            else :
                count+=1
                prev+=1
        return count        
                ```