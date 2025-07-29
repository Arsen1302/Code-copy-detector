class Solution:
    def solution_725_5(self, s: str) -> str:
        # Initiate a blank list
		str_list = []
        for i in s:
            # Remove the element from that list only if its Non Empty and its last appended element = current element
			if str_list and str_list[-1] == i:
                str_list.pop()
            else:
			    # Else, keep appending the characters
                str_list.append(i)
        return ''.join(str_list)