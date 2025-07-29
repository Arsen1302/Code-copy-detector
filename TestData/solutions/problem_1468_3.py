class Solution:
    def solution_1468_3(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        no_of_groups = math.ceil(len(s)/k)
        start = 0
        while no_of_groups>0:
            if s[start:start+k]:
                ans.append(s[start:start+k])
            else:
                ans.append(s[start:])
            start+=k
            no_of_groups-=1
        while len(ans[-1])!=k:
                ans[-1]+=fill           
        return ans