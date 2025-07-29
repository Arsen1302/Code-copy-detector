class Solution:
    def solution_1648_5(self, num: str) -> str:
        count = Counter(num)
        fre = ''.join(count[i]//2*i for i in '9876543210')
        mid = max(count[i]%2 * i for i in count)
        return (fre +mid + fre[::-1]).strip('0') or '0'