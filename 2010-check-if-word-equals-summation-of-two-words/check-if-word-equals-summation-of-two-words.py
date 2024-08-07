class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        firstnumber = []
        secondnumber = []
        targetnumber = []
        for char in firstWord:
            firstnumber.append(ord(char) - 97)
        for char in secondWord:
            secondnumber.append(ord(char) - 97)
        for char in targetWord:
            targetnumber.append(ord(char) - 97)
        
        firstnumber = [str(t) for t in firstnumber]
        firstnumber = ''.join(firstnumber)
        firstnumber = int(firstnumber)

        secondnumber = [str(t) for t in secondnumber]
        secondnumber = ''.join(secondnumber)
        secondnumber = int(secondnumber)

        targetnumber = [str(t) for t in targetnumber]
        targetnumber = ''.join(targetnumber)
        targetnumber = int(targetnumber)

        if firstnumber + secondnumber == targetnumber:
            return True
        else:
            return False
        



        
        