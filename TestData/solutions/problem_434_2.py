class Solution:
    def solution_434_2(self, left: int, right: int) -> List[int]:
        v = []
        for x in range(left, right+1):
            # iterate thru every number left-right

            a = [*str(x)]
            # basically splits the str version of the number
            # ex: 22 -> ['2','2']

            d = True
            # bool variable to validate every number is self dividing

            for r in a:
                if int(r) != 0:
                # making sure r is not something like '0' in something like 10 for example
                    if x%int(r)!=0:
                        # if there is a number thats remainder is not 0
                        d = False
                else:
                    d = False
                    # falsing when there is a number such as 10, 20
            if d:
                v.append(x)
                # if d ends up being true, it appends x to v
        return v