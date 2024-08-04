class Solution(object):
    def judgeCircle(self, moves):
        dictt = {}
        for i in moves:
            if i in dictt:
                dictt[i] += 1
            else:
                dictt[i] = 1
        for k in ['U','D','L', 'R']:
            if k in dictt:
                continue
            else:

                dictt[k] = 0
        if dictt['U'] == dictt['D'] and dictt['L'] == dictt['R']:
            return True
        return False
            
        