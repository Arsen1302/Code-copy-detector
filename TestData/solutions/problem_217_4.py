class Solution:
def solution_217_4(self, people: List[List[int]]) -> List[List[int]]:
    ans = []
    for p in sorted(people, key=lambda p: (-1 * p[0], p[1])):
        ans.insert(p[1], p)
    return ans