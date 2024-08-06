class Solution(object):
    def squareIsWhite(self, coordinates):
        horizontal = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
        if (horizontal[coordinates[0]] % 2 == 0 and int(coordinates[1]) % 2 == 0) or (horizontal[coordinates[0]] % 2 != 0 and int(coordinates[1]) % 2 != 0):
            return False
        elif (horizontal[coordinates[0]] % 2 != 0 and int(coordinates[1]) % 2 == 0) or (horizontal[coordinates[0]] % 2 == 0 and int(coordinates[1]) % 2 != 0):
            return True
        