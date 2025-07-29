class Solution:
    def solution_631_4(self, deck: List[int]) -> List[int]:
        d = sorted(deck, reverse=1)
        res = [d[0]]
        d.pop(0)
        while(d):
            # 1. move the bottom to the top
            btn = res.pop(-1)
            res.insert(0, btn)
            # 2. add a card to the top
            card = d.pop(0)
            res.insert(0, card)
        return res