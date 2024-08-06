class Solution(object):
    def peakIndexInMountainArray(self, arr):
        peak = max(arr)
        return arr.index(peak)
        