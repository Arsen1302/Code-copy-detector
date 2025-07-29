class Solution:
    def solution_1013_4(self, date: str) -> str:
        date = date.split()
        d = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        if int(date[-3][:-2]) < 10:
            date[-3] = "0"+date[-3]
        return date[-1]+"-"+d[date[-2]]+"-"+date[-3][:-2]