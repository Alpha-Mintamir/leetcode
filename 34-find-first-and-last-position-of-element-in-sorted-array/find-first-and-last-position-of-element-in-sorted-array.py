class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def fromLeft():
            L, R = 0, len(nums)-1
            found = -1
            while(L<=R):
                mid = (L+R)//2
                if target == nums[mid]:
                    found = mid
                    R = mid-1
                elif(target>nums[mid]):
                    L = mid+1
                else:
                    R = mid-1
            return found
        def fromRight():
            L, R = 0, len(nums)-1
            found = -1
            while(L<=R):
                mid = (L+R)//2
                if target == nums[mid]:
                    found = mid
                    L = mid+1
                elif(target>nums[mid]):
                    L = mid+1
                else:
                    R = mid-1
            return found

        return([fromLeft(),fromRight() ])


            
            

        