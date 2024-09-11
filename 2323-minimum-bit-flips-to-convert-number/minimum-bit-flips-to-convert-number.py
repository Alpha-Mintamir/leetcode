class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = bin(start).replace("0b", "")
        goal = bin(goal).replace("0b", "")
        nstart = len(start)
        ngoal = len(goal)
        ndiff = abs(nstart-ngoal)
        zeros = []
        result = 0
        if ndiff != 0:
            for i in range(ndiff):
                zeros.append(0)
        start = list(map(int, str(start)))
        goal = list(map(int, str(goal)))
        if nstart>ngoal:
            goal = zeros + goal
        elif nstart<ngoal:
            start = zeros + start
        for i, j in zip(start, goal):
            if i!=j:
                result += 1
        return result

            



        