class Solution:
    def solution_749_3(self, label: int) -> List[int]:
        level = int(log2(label))
        compl = 3*2**level - 1 - label # complement 
        
        ans = []
        while label: 
            ans.append(label)
            label //= 2
            compl //= 2
            label, compl = compl, label
        return ans[::-1]