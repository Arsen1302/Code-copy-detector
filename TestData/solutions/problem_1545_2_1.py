class Solution:
    def solution_1545_2_1(self, s: str, k: int) -> str:
        def solution_1545_2_2(s: str, k: int) -> List[str]: # Utility function to return list of divided groups.
            l, n = [], len(s)
            for i in range(0, n, k):
                l.append(s[i:min(i + k, n)])
            return l
        while len(s)>k: # Till size of s is greater than k
            arr, temp = solution_1545_2_2(s, k), [] # arr is the list of divided groups, temp will be the list of group sums
            for group in arr: # Traverse the group and add its digits
                group_sum = 0
                for digit in group:
                    group_sum += int(digit)
                temp.append(str(group_sum)) # Sum of digits of current group
            s = ''.join(temp) # s is replaced by the group digit sum for each group.
        return s