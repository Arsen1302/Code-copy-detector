class Solution:
    def solution_1258_4(self, s: str) -> bool:
        s = s.lstrip("0")
        if s:
            for end in range(1, len(s)):
                next_num = str(int(s[:end]) - 1)
                remaining_s = s[end:]
                if set(remaining_s) == {"0"}:
                    remaining_s = "0"
                else:
                    remaining_s = remaining_s.lstrip("0")
                while remaining_s and remaining_s.startswith(next_num):
                    remaining_s = remaining_s[len(next_num):]
                    if set(remaining_s) == {"0"}:
                        remaining_s = "0"
                    else:
                        remaining_s = remaining_s.lstrip("0")
                    next_num = str(int(next_num) - 1)
                if not remaining_s:
                    return True
        return False