class Solution:
    def solution_408_5_1(self, stickers: List[str], target: str) -> int:

        stickers = [Counter(s) for s in stickers if set(s)&amp;set(target)]
        def solution_408_5_2(target):
            if not target: return 0
            
            target_counter = Counter(target)
            res = float("inf")
            for sticker in stickers:
                if sticker[target[0]] == 0: continue
                tmp = 1 + solution_408_5_2("".join([letter*count for letter,count in (target_counter-sticker).items()]))

                res = min(res,tmp)
            return res

        res = solution_408_5_2(target)
        return -1 if res == float("inf") else res