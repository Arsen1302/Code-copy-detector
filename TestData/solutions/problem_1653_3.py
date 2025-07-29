class Solution:
    def solution_1653_3(self, garbage: List[str], travel: List[int]) -> int:
			# add 0 to prefix because for the first house the commute time is 0
            prefix = [0]
            cur = 0
            for time in travel:
                cur += time
                prefix.append(cur)
			# the default index is zero
			# it does not mean each grabage appears in the first house, only for calculation convenience
            M_idx, G_idx, P_idx = 0, 0, 0
            res = 0
            for i in range(len(garbage)):
                res += len(garbage[i])
                if "M" in garbage[i]:
                    M_idx = i
                if "G" in garbage[i]:
                    G_idx = i
                if "P" in garbage[i]:
                    P_idx = i
            res += prefix[M_idx]
            res += prefix[G_idx]
            res += prefix[P_idx]
            
            return res