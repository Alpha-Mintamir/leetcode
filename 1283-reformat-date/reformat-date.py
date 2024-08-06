class Solution(object):
    def reformatDate(self, date):
        result = []
        month = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
        date = date.split()
        date = list(reversed(date))
        result.append(date[0])
        result.append(month[date[1]])
        if len(date[2])==3:

            result.append('0' + date[2][:1])
        elif len(date[2])==4:

            result.append(date[2][:2])

        return '-'.join(result)
        