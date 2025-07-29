class Solution:
    def solution_950_4(self, croakOfFrogs: str) -> int:
        string = "croak"
        cnt = [0] * len(string)
        res, cur = 0, 0
        for c in croakOfFrogs:
            index = string.index(c)
            cnt[index] += 1
            # current char cnt should be greater than previous
            if index > 0 and cnt[index] > cnt[index-1]:
                return -1
            # new singing, increasing cur cnt
            if c == "c":
                cur += 1
            # singing finished, decreasing
            if c == "k":
                cur -= 1
            # capture max concurrent singing frogs
            res = max(res, cur)
        # all element should be the same
        if max(cnt) != min(cnt):
            return -1
        return res