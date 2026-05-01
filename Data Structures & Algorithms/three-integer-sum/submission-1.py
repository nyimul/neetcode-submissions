class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Instead of using two pointers as anchors, we anchor at one index,
        # then use the two pointers to check the rest of the array, while
        # avoiding duplicates. You did not get this at first.

        # Use dictionary to get rid of any duplicates maybe? Not needed
        # if we traverse optimally
        # But we would need to sort for this to work
        # dictForDupes = {}

        # Sort it here because we want to optimize how we move pointers.
        output = []
        nums.sort()
        for index in range(len(nums)-2):
            # CHECK FOR DUPES for anchor
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            left = index+1
            right = len(nums)-1
            while (left < right):
                if (nums[index] + nums[left] + nums[right] > 0):
                    # Too big, we move the right pointer to decrese
                    right -= 1
                elif (nums[index] + nums[left] + nums[right] < 0):
                    # Too small
                    left += 1
                else:
                    # We got one
                    addThis = [nums[index], nums[left], nums[right]]
                    output.append(addThis)
                    # Still need to move pointers:
                    # Move them until we dont have a dupe?
                    # But we need to check if in bounds
                    while (left < right and nums[left] == nums[left+1]):
                        left += 1
                    while (right > left and nums[right] == nums[right-1]):
                        right -= 1
                    # Still need to move after skipping dupes
                    left += 1
                    right -= 1
        return output


