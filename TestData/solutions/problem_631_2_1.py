class Solution:
    def solution_631_2_1(self, deck: List[int]) -> List[int]:
        def solution_631_2_2(n):
            lst = list(range(n))
            ans = []
            i = 0
            while lst:
                if not i&amp;1: ans.append(lst.pop(0))
                else: lst.append(lst.pop(0))
                i += 1
            return ans
        ans = solution_631_2_2(len(deck))
        ans = sorted([v, i] for i, v in enumerate(ans))
        deck.sort()
        return (deck[j] for i,j in ans)