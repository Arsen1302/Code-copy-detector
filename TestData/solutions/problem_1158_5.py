class Solution:

    # get all the powers of two
    powers = set([2**exp for exp in range(22)])

    def solution_1158_5(self, deliciousness: List[int]) -> int:

        # count the number of occurences
        cn = collections.Counter(deliciousness)

        # iterate over the combinations
        result = 0
        for item, amount in cn.items():

            # get all the self pairs
            if item in self.powers:
                result += amount*(amount-1)//2
            
            # check for all powers of two
            # if our counterpart has values
            for power in self.powers:
                if power > 2*item:
                    result += cn[power - item]*amount
        return result % 1_000_000_007