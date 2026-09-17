class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum_element = nums[0]

        l = 0
        r = len(nums) - 1


        while (l <= r):
            

            if (nums[l] < nums[r]):
                minimum_element =  min(minimum_element, nums[l])
                break

            middle = (l + r)//2
            minimum_element = min(minimum_element, nums[middle])

            if (nums[middle] >= nums[l]):
                l = middle + 1
            
            else:
                r = middle - 1
        
        return minimum_element
            


