class Solution:
    def solution_1145_4(self, number: str) -> str:
		# Written by LeetCode user DyHorowitz
        # remove the unnecessary characters - we don't care about the dashes nor spaces
        number =  number.replace('-', '')
        number = number.replace(' ', '')
        
        # set up a return string to store our answer into
        returnString = ""
        
        # So long as there are more than 4 digits in number,
        # we want to group the first 3 into our return string
        # followed by a dash, then remove those 3 from the initial string
        while len(number) > 4:
            returnString += number[0:3] + "-"
            number = number[3:]
        
        # If there are only three digits left, we just put them all into 
        # the return string and are done
        if len(number) == 3:
            returnString += number[0:3]
            
        # A remainder of 4 or 2 will result in blocks of 2, so
        # we might as well combine these two possibilities 
        # for the first part and save some computing time
        else:
            returnString += number[0:2]
            number = number[2:]
            
            # This is where we test if there were 4 or 2 digits 
            # left over. If there were 2, then removing the last
            # 2 in the step above should leave us with a string
            # of length 0
            if len(number) > 0:
                returnString += "-" + number
        
        # Note that we only created ONE new variable in this entire function:
        # "returnString". By having 'number' overwrite itself, we save
        # significantly on memory space (you could probably save even more)
        # by using recursion to avoid storing any variables, however
        # that may come at the cost of processing time
        return returnString