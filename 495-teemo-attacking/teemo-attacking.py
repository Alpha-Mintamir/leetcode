class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        count=0
        for i in range(len(timeSeries)):
            if(i<len(timeSeries)-1):
                if(timeSeries[i]+duration-1<timeSeries[i+1]):
                    count+=duration
                elif(timeSeries[i]+duration-1==timeSeries[i+1]):
                    count+=timeSeries[i+1]-timeSeries[i]
                else:
                    count+=timeSeries[i+1]-timeSeries[i]
            else:
                count+=duration
        return(count)