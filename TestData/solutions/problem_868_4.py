class Solution:
    def solution_868_4(self, n):
        for x in range(1, n):
            for c in str(x):
                if c == '0':
                    break
            else:
                for y in str(tmp := n - x):
                    if y =='0':
                        break
                else:
                    return x, tmp