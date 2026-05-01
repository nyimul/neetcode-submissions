class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Solve with division:
        #Get the product of everything then divide by nums[i]
        # unless it is a 0. Still need to capture a product
        # O(2n)
        product = 1
        zeroCount = 0
        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                product *= num
        for i in range(len(nums)):
            if zeroCount > 1:
                # Everything gotta be zero
                nums[i] = 0
            elif zeroCount == 1:
                # Everything ELSE has to be zero
                if nums[i] == 0:
                    nums[i] = product
                else:
                    nums[i] = 0
            else:
                # Zero zeros, so normal logic
                nums[i] = product // nums[i]
        return nums