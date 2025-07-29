class Solution:
    def solution_217_5(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: [-x[0], x[1]])
        ans = []
        for h, k in people:
            ans = ans[:k] + [[h, k]] + ans[k:]
        return ans