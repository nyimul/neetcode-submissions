class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # No division solution - we want to avoid recomputation
        # FOR EACH index in NUMS:
        # compute a "left"/"prefix" array where its equivalent index
        # is the product of all nums to the left
        # and compute a "right"/"postfix" array where its equivalent
        # index is the product of all nums to the right.
        # Edge cases: first num in leftArray is 1, last num in rightArray is 1

        # Left Array
        leftArray = []
        leftProduct = 1
        for index, num in enumerate(nums):
            if (index == 0):
                leftArray.append(1)
            else:
                # leftArray[index] = leftArray[index-1]*leftArray[index]
                leftArray.append(leftArray[index-1] * nums[index-1])
                # You forgot nums[index-1]**************************************
        #print("Left Array: ", leftArray)

        # Right array; iterating backwards with placeholder [1]'s
        rightArray = [1] * len(nums) # HOW TO CREATE A PLACEHOLDER ARRAY HERE
        # Iterate backwards with weird bounds and stuff
        for index in range(len(nums)-1, -1, -1):
            if (index == len(nums)-1):
                rightArray[index] = 1
            else:
                rightArray[index] = rightArray[index+1] * nums[index+1]
        #print("Right Array: ", rightArray)

        #return rightArray * leftArray
        # Need to do element wise product
        output = []
        for left, right in zip(leftArray, rightArray):
            output.append(left * right)
        return output


        # # Right Array, reversed after making it. FAILED!!!!!
        # rightArray = []
        # rightProduct = 1
        # for index, num in enumerate(reversed(nums)):
        #     if (index == 0):
        #         rightArray.append(1)
        #     else:
        #         rightArray.append(rightArray[index-1] * nums[index-1])
        # rightArray = reversed(rightArray)
        # print("Right Array: ", rightArray)

        # # Trying to do it all at once. FAILED!!!!!
        # for index, num in enumerate(nums):
        #     # Left Array and Right Array edge cases:
        #     if (index == 0):
        #         leftArray[index] = 1
        #     elif (index == len(nums) - 1):
        #         rightArray[index] = 1
