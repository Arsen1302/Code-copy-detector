class Solution:
    def solution_230_4(self, s: str) -> str:
        freq = Counter(s)
        res = {}
        res["0"] = freq["z"]
        res["2"] = freq["w"]
        res["4"] = freq["u"]
        res["6"] = freq["x"]
        res["8"] = freq["g"]
        res["3"] = freq["h"] - res["8"]
        res["5"] = freq["f"] - res["4"]
        res["7"] = freq["s"] - res["6"]
        res["9"] = freq["i"] - res["5"] - res["6"] - res["8"]
        res["1"] = freq["n"] - res["7"] - (2 * res["9"])
        num = ""
        for i in res:
            if res[i] != 0:
                num += i * res[i]
        return ''.join(sorted(num))