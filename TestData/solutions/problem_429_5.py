class Solution:
    def solution_429_5(self, accounts: List[List[str]]) -> List[List[str]]:
        tagged = {}
        for cur_group in accounts:
            for mail in cur_group[1:]:
                if mail not in tagged:
                    tagged[mail] = cur_group
                orig_group = tagged[mail]
                if orig_group is cur_group:
                    continue
                cur_group.extend(orig_group[1:])
                for mail in orig_group[1:]:
                    tagged[mail] = cur_group
                orig_group[0] = None
        return [[group[0],] + sorted(list(set(group[1:]))) for group in accounts if group[0] is not None]