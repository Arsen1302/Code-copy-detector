class Solution:
    def solution_751_3_1(self, expression: str) -> bool:
		# eval function would treat f and t as variables. Assign False and True to them.
        f = False
        t = True
        
		# convert | into an OR function
        def solution_751_3_2(*args):
            return reduce(lambda x,y:x or y, args)
        
		# convert &amp; into an AND function
        def solution_751_3_3(*args):
            return reduce(lambda x,y : x and y, args)
        
		# no need to create a not function as ! only takes one argument anyway
		# replace &amp; and | with the function names. And run eval
        return eval(expression.replace('|','solution_751_3_2').replace('&amp;', 'solution_751_3_3').replace('!', 'not'))