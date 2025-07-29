class Solution:
    def solution_534_5(self, hand: List[int], k: int) -> bool:
        n = len(hand)
        if n%k != 0:
            return False
        
        d = {}
        for i in hand:
            d[i] = d.get(i, 0) + 1
        
        while d:
            mn = min(d.keys())
            for i in range(k):
                if (mn+i) in d:
                    if d[(mn+i)] == 1:
                        del d[(mn+i)]
                    else:
                        d[(mn+i)] -= 1
                else:
                    return False
        
        return True