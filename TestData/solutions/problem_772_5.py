class Solution:
	def solution_772_5(self, date: str) -> int:
		map={
			0:0,
			1:31,
			2:28,
			3:31,
			4:30,
			5:31,
			6:30,
			7:31,
			8:31,
			9:30,
			10:31,
			11:30,
			12:31                
		}

		year=int(date.split('-')[0])
		month=date.split('-')[1]
		day=date.split('-')[2]

		days=0
		for x in range(0,int(month)):
			days+=map.get(int(x))

		if not  year % 400:
			is_leap_year = True
		elif not year % 100:
			is_leap_year = False
		elif not year % 4:
			is_leap_year = True
		else:
			is_leap_year = False

		if is_leap_year and int(month)>2:
			return days+int(day)+1
		else:
			return days+int(day)