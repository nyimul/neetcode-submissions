class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Go through array and store values in Hashmap
        #create map
        map = {}
        for index, num in enumerate(nums):
            # Check for duplicate
            if (num in map):
                return True
            # Otherwise it isn't in it
            map[num] = index
        # Exit loop, return False
        return False
