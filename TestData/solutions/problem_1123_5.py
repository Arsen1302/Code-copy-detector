class Solution:
    def solution_1123_5(self, n: int, k: int) -> str:
        ans = ['a'] * n
        k, i = k-n, n-1
        z, nz = divmod(k, 25)                # `z`: number of *z* I need, `nz`: ascii of the letter just to cover the leftover
        ans[n-1-z] = chr(nz + ord('a'))      # adjust the left over `k` using mod
        return ''.join(ans[:n-z]) + 'z' * z  # make final string &amp; append `z` to the end