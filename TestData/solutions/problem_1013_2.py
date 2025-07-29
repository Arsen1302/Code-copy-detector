class Solution:
    def solution_1013_2(self, date: str) -> str:
        months = {
            'Jan' : '01',
            'Feb' : '02',
            'Mar' : '03',
            'Apr' : '04',
            'May' : '05',
            'Jun' : '06',
            'Jul' : '07',
            'Aug' : '08',
            'Sep' : '09',
            'Oct' : '10',
            'Nov' : '11',
            'Dec' : '12',
        }

        day, month, year = date.split()

        day = day[ : -2 ] # remove st or nd or rd or th
        day = '0' + day if len( day ) == 1 else day # needs to be 2 digits

        return year + '-' + months[ month ] + '-' + day