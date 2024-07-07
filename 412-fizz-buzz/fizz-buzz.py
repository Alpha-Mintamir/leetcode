class Solution(object):
    def fizzBuzz(self, n):
        newList = []
        for i in range(1,n+1):
            if(i%3==0 and i%5==0):
                newList.append("FizzBuzz")
            elif i% 3==0:
                newList.append("Fizz")
            elif i%5==0:
                newList.append("Buzz")
            else:
                newList.append(str(i))
        return newList

        