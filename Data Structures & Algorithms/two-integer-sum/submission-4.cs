public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        // target = thisNum + thisNum'sComplement
        Dictionary<int, int> seen = new();
        for (int i = 0; i < nums.Length; i++) {
            int complement = target - nums[i];
            if (seen.TryGetValue(complement, out var index)) {
                return [seen[complement], i];
            }
            // Else we just need to add to seen map
            seen[nums[i]] = i;
        }
        return [];
    }
}
