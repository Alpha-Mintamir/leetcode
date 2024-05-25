class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)
        if k > n:
            print("invalid")
            return -1

        win_sum = sum(nums[:k])
        max_sum = win_sum / float(k)

        for i in range(1, n - k + 1):  
            win_sum = win_sum - nums[i - 1] + nums[i + k - 1]
            max_sum = max(max_sum, win_sum / float(k))

        return max_sum
