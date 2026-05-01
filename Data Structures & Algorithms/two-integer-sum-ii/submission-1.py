class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # This didnt come naturally to you
        # Move left or right dependent on currentSum
        left = 0
        right = len(numbers) - 1
        currentSum = numbers[left] + numbers[right]
        while currentSum != target:
            if (currentSum > target):
                right -= 1
                currentSum = numbers[left] + numbers[right]
            elif (currentSum < target):
                left += 1
                currentSum = numbers[left] + numbers[right]
            else:
                break
        return [left + 1, right + 1]