public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        // target = current num + its complement
        // always be coding
        Dictionary<int, int> seen = new();
        for (int i = 0; i < nums.Length; i++) {
            int complement = target - nums[i];
            if (seen.TryGetValue(complement, out var j)) {
                return [j, i];
            }
            seen[nums[i]] = i;
        }
        return [];
    }
}
