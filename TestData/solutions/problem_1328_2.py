class Solution:
    def solution_1328_2(self, num: str, change: List[int]) -> str:

        # make a list from the string for a mutable datatype
        num = list(num)

        # go through the number and start mutating as soon as
        # we hit a number that becomes bigger
        # mark as mutating since we started mutation
        # end the loop if we encounter a number that would
        # get smaller by mutating
        mutated = False
        for idx, n in enumerate(num):

            # get the current digit
            n = int(n)
            if change[n] > n:
                num[idx] = str(change[n])
                mutated = True
            elif change[n] < n and mutated:
                break
        return "".join(num)