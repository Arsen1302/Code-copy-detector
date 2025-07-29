class Solution:
    #example 1 
    #result =[(1&amp;6)^(1&amp;5)^(2&amp;6)^(2&amp;5)^(3&amp;6)^(3&amp;5)]
                \     /     \    /      \     /
    #           (1&amp;(6^5)) ^ (2&amp;(6^5)) ^ (3&amp;(6^5))   
                   \            |           /
                    \           |          /
                     \          |         /
                      \         |        /
    #                  ((1^2^3) &amp; (6^5))
    def solution_1249_1(self, a, b):
        x = 0 
        for i in range(len(a)):
            x = x ^ a[i]
        y = 0 
        for j in range(len(b)):
            y = y ^ b[j]
        return x &amp; y