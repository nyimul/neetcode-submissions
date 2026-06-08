class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for index, value in enumerate(nums):
            complement = target - value
            if (complement in m):
                # Success
                return [m.get(complement) , index]
            # No complement found, so add to map
            m[value] = index
        return [0, 0]