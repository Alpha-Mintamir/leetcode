class Solution(object):
    def interpret(self, command):
        result = []
        for i in range(len(command)):
            if command[i] == "G":
                result.append("G")
            elif command[i] == "(":
                if command[i+1] == ")":
                    result.append("o")
                elif command[i+1] == "a":
                    result.append("al")
        return ''.join(result)
        