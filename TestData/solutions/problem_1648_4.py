class Solution:
    def solution_1648_4(self, num: str) -> str:
        cnt = Counter(num)
        left = middle = ""
        for c in "987654321":
            n, r = divmod(cnt[c], 2)
            if n:
                left += c * n
            if not middle and r:
                middle = c
        n, r = divmod(cnt["0"], 2)
        if left and n:
            left += "0" * n
        if not middle and r or not left and n and not middle:
            middle = "0"
        return f"{left}{middle}{left[::-1]}"