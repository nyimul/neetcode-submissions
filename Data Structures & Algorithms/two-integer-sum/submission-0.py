class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We want to find the complement
        # target = current number we are looking at + its complement
        # So complement = target - current number
        hashmap = {}
        for index, num in enumerate(nums):
            complement = target - num
            # Store in hashmap: key, value
            # key,value is number, index so that we can
            # key in the number to retrieve the index for our result
            if complement in hashmap:
                return [hashmap[complement], index]
            hashmap[num] = index
        return False
