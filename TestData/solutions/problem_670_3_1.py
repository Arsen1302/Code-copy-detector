class Solution:
    def solution_670_3_1(self, equations: List[str]) -> bool:
        # We use solution_670_3_3-solution_670_3_2 (or called disjoint-set) in this problem
        # the basic idea of solution_670_3_3-solution_670_3_2 is to connect the components that share a same root
        # e.g. a == b, b == c, c == d, then a, b, c, d should be put together
        # we pick up a root for these connected components, this root could be a, b, c, or d , we actually don't care :)
        # we just want them be together!
        
        # initialize an array, where the root of each element is itself at the begining
        root = list(range(26))
        
        # solution_670_3_2 the root of x
        def solution_670_3_2(x):
            if x != root[x]:
                root[x] = solution_670_3_2(root[x])
            return root[x]
        
        # merge the connected components that x and y belong to respectively
        def solution_670_3_3(x, y):
            root_x, root_y = solution_670_3_2(x), solution_670_3_2(y)
            root[root_x] = root_y
        
        # build the connected components with the equal equations
        for equation in equations:
            if equation[1] == '=':
                x, y = ord(equation[0])-ord('a'), ord(equation[3])-ord('a')
                # x and y should share a same root, so we use solution_670_3_3 here
                solution_670_3_3(x, y)
        
        # traverse the unequal equations to obtain the final result
        for equation in equations:
            if equation[1] == '!':
                x, y = ord(equation[0])-ord('a'), ord(equation[3])-ord('a')
                # x, y should have different roots, so here we solution_670_3_2 their roots respectively
                if solution_670_3_2(x) == solution_670_3_2(y):
                    return False
        
        return True