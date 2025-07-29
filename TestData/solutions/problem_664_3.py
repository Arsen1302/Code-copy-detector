class Solution:
    def solution_664_3(self, a: int, b: int) -> str:
        n = a + b
        fill = 'a' if a >= b else 'b'
        ma = a if a >= b else b
        mi = a if a < b else b
        string = [None]*n
        index = 0
        while ma > 0 :
            string[index] = fill
            index += 3
            if index >= n: index = 1
            ma -= 1
        fill ='a' if a < b else 'b'
        ans = ""
        for i in string:
            if i == None: ans += fill
            else: ans += i
        return ans