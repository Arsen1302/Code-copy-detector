class Solution:          # A few points on the problem:
                         #   • The start and end is a "red herring." The answer to the problem 
                         #     depends only on the distance (dist = end-start) and k.
                         #  
                         #   • A little thought will convince one that theres no paths possible 
                         #     if k%2 != dist%2 or if abs(dist) > k.

                         #   • The problem is equivalent to:
                         #        Determine the count of distinct lists of length k with sum = dist
                         #        and elements 1 and -1, in which the counts of 1s and -1s in each 
                         #        list differ by dist.
                         # 
                         #   • The count of the lists is equal to the number of ways  the combination 
                         #     C((k, (dist+k)//2)). For example, if dist = 1 and k = 5. the count of 1s
						 #.    is (5+1)//2 = 3, and C(5,3) = 10.
                         #     (Note that if dist= -1 in this example, (5-1)//2 = 2, and C(5,2) = 10)

    def solution_1660_1(self, startPos: int, endPos: int, k: int) -> int:

        dist = endPos-startPos

        if k%2 != dist%2 or abs(dist) > k: return 0

        return comb(k, (dist+k)//2) %1000000007