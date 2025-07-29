class Solution:
    def solution_964_3(self, target: List[int], n: int) -> List[str]:
        ans = []
        arr = []
        for i in range(1,n+1):
            if i in target:
                ans.append("Push")
                arr.append(i)
            else:
                ans.append("Push")
                ans.append("Pop")
            if arr == target:
                return ans
        return ans