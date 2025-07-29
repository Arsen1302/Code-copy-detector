class Solution:
    def solution_811_1(self, folder: List[str]) -> List[str]:
        ans = []
        for i, path in enumerate(sorted(folder)):
            if i == 0 or not path.startswith(ans[-1] + "/"):
                ans.append(path)
        return ans