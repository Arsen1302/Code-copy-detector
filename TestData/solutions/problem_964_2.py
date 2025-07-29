class Solution:
    def solution_964_2(self, target: List[int], n: int) -> List[str]:
        output = []
        new_target = []
        l = [i for i in range(1,n+1)]
        for i in l:
            if new_target == target:
                return output
            output.append("Push")
            new_target.append(i)
            if i not in target:
                output.append("Pop")
                new_target.pop()
        return output