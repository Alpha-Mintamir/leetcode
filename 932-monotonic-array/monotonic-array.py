class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        check = 0  # 0 means unknown, 1 means increasing, -1 means decreasing

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # increasing
                if check == 0:
                    check = 1
                elif check == -1:
                    return False
            elif nums[i] < nums[i - 1]:  # decreasing
                if check == 0:
                    check = -1
                elif check == 1:
                    return False

        return True