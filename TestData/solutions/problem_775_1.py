class Solution:
#     O(n^2) || O(1)
# Runtime: 96ms 97.20% Memory: 14.5mb 84.92%
    def solution_775_1(self, words: List[str], chars: str) -> int:
        ans=0
        for word in words:
            for ch in word:
                if word.count(ch)>chars.count(ch):
                    break
            else:
                ans+=len(word)
        
        return ans