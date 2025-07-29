class Solution:
#     O(n) || O(n)
# Runtime: 77ms 53.47% ; Memory: 14.7mb 41.07%
    def solution_276_5(self, string: str, k: int) -> str:
        newString = string.upper().replace('-', '')[::-1]
        group = []
        for i in range(0, len(newString), k):
            group.append(newString[i:i+k])
        
        return '-'.join(group)[::-1]