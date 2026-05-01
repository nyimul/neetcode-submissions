class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Solve with division:
        #Get the product of everything then divide by nums[i]
        # unless it is a 0. Still need to capture a product
        # O(2n)
        product = 1
        # hasZero = False
        zeroCount = 0
        for num in nums:
            if num == 0:
                #Skip and check again later
                #hasZero = True
                #continue
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

            # if (nums[i] == 0):
            #     # everything else should be 0
            #     nums[i] = product
            # else:
            #     if hasZero:
            #         nums[i] = 0
            #     else:
            #         nums[i] = product / nums[i]
            #         nums[i] = int(nums[i])
        return nums