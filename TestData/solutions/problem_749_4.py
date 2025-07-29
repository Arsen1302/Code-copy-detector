class Solution:
    def solution_749_4(self, label: int) -> List[int]:
        ret = [label]
        height = int(math.log(label,2))
        prev = 1<<height
        while height:
            right = prev-1         # 2^height-1
            left = prev = prev//2  # 2^(height-1)
            label = left+right-label//2
            ret.append(label)
            height -= 1
        return ret[::-1]