class Solution:
    def solution_169_5(self, words: List[str]) -> List[List[int]]:
        re_dict = {w[::-1]: idx for idx, w in enumerate(words)}
        ret = []
        for w_idx, w in enumerate(words):
            for idx in range(0, len(w)+1):
                prefix = w[:idx]
                if prefix in re_dict:
                    if re_dict[prefix] != w_idx:
                        remaining = w[idx:]
                        if remaining == remaining[::-1]:
                            ret.append([w_idx, re_dict[prefix]])
        for w_idx, w in enumerate(words):
            for idx in range(0, len(w)+1):
                suffix = w[idx:]
                if suffix in re_dict:
                    if re_dict[suffix] != w_idx and len(words[re_dict[suffix]]) != len(words[w_idx]):
                        remaining = w[:idx]
                        if remaining == remaining[::-1]:
                            ret.append([re_dict[suffix], w_idx])

        return ret