class Solution:
    def solution_1509_3(self, s: str) -> int:
        '''
            Intuition: Start on the outer corners, moving in from left and right, and do min swaps to make them the same.

            Spacetime: O(n)
            Runtime: O(n^2)
        '''

        i, j = 0, len(s) - 1
        sArr = list(s)
        swaps = 0

        while i < j:
            if sArr[i] != sArr[j]:
                minSwapsI = math.inf # min swaps needed to get i the same as position j
                minSwapsJ = math.inf

                # get min swaps needed to make pos i == pos j
                for k in range(i+1,j):
                    if sArr[k] == sArr[j]:
                        minSwapsI = k - i
                        break

                # get min swaps needed to make pos j == pos i
                for k in range(j-1, i, -1):
                    if sArr[k] == sArr[i]:
                        minSwapsJ = j - k
                        break
                
                # make min swaps needed
                if minSwapsI < minSwapsJ:
                    for k in range(i + minSwapsI, i, -1):
                        sArr[k-1], sArr[k] = sArr[k], sArr[k-1]
                else:
                    for k in range(j - minSwapsJ, j):
                        sArr[k+1], sArr[k] = sArr[k], sArr[k+1]
                
                swaps += min(minSwapsI, minSwapsJ) # update swap count

            # update pointers
            i += 1
            j -= 1

        return swaps