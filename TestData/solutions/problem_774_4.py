class Solution:
    def solution_774_4(self, text: str) -> int:
        lst = [(key, len(list(seq))) for key, seq in groupby(text)]
        len_lst_2 = len(lst) - 2
        cnt = Counter(text)
        max_len = 0
        for i, (key, n) in enumerate(lst):
            max_len = max(max_len, n)
            if n < cnt[key]:
                max_len = max(max_len, n + 1)
            if i < len_lst_2 and lst[i + 1][1] == 1 and lst[i + 2][0] == key:
                if (len_both := n + lst[i + 2][1]) < cnt[key]:
                    max_len = max(max_len, len_both + 1)
                else:
                    max_len = max(max_len, len_both)
        return max_len