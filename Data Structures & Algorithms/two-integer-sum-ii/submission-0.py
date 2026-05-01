class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Optimal solution: Use the idea that it is non-decreasing order.
        # One left pointer, and one right pointer. Move one pointer inwards as we approach target

        #This one did not come naturally to you
        
        left = 0
        right = len(numbers)-1
        currentSum = numbers[left] + numbers[right]
        # Left pointer
        while currentSum != target:
            if (currentSum > target):
                # Too big, move right
                print("hit it")
                right -= 1
                print(right)
                currentSum = numbers[left] + numbers[right]
                print(currentSum)
            elif (currentSum < target):
                # Too small, move left
                left += 1
                currentSum = numbers[left] + numbers[right]
            else:
                # CurrentSum is equal
                return [left + 1, right + 1]
        return [left + 1, right + 1]
