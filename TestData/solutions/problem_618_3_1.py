class Solution:
    def solution_618_3_1(self, logs: List[str]) -> List[str]:
        return logs.sort(key= lambda log: self.solution_618_3_2(log))
        
    def solution_618_3_2(self, log: str) -> tuple:
		#seperate identifer and suffix into two seperate arrays
        log_info = log.split(" ", 1)
		#check if log is a letter or digital log by checking index in suffix array
		# we return 1 as tuple so that digits will always appear after letters and so that when to digits are compared
		# we can leave them in their original position
        if log_info[1][0].isdigit():
            return 1,
		#We use a zero to make sure that when compared against a digit we can guranatee that our letter will appear first
		#We use the suffix as the next condition and the identifier as the last condition if theres a tie
        return 0,log_info[1],log_info[0]