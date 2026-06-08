class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Java solution
        // Brute force: loop through once, and for each index, check the rest of the array. This is O(n^2)
        // Better solution: currentValue + itsComplement = target. We are looking for complement
        // complement = target - currentValue, this is what we search for via hashmap, i.e. "Have we already seen the complement we want?"
        // Hashmap keeps: values:its index
        /*
        Example: nums = [4,5,6], target = 10
        complement = target - currentValue:
        [4]: complement = 10-4 = 6. Hashmap does not contain 6, we store 4:0.
        [5]: complement = 10-5 = 5: Hashmap does not contain 5, we store 5:1.
        [6]: complement = 10-5 = 4: Hashmap DOES contain 4. We use it to get 4's index of 0, and return [0,2].
        */
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                // Success, return pair
                int[] answer = {map.get(complement), i};
                return answer;
            }
            // No complement in the hashmap so we store.
            map.put(nums[i], i);
        }
        return null;
    }
}
