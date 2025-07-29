class Solution:
    def solution_1013_5(self, date: str) -> str:
        months_dict = {"Jan": "01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        parts = date.split(' ')
        
        parts[1] = months_dict[parts[1]]
        parts[0] = parts[0][:-2]
        
        if len(parts[0]) == 1:
            parts[0] = '0' + parts[0]
        
        return '-'.join(reversed(parts))