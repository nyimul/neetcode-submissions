// Dont need imports in neetcode, but looks like this:
//import java.util.HashSet;
class Solution {
    public boolean hasDuplicate(int[] nums) {
        // Use a simple set
        /*
        java comments
        */
        Set<Integer> uniqueNums = new HashSet<>();
        
        for (int i = 0; i < nums.length; i++) {
            //System.out.println(i);
            if (uniqueNums.contains(nums[i])) {
                // contains a duplicate!
                return true;
            }
            uniqueNums.add(nums[i]);
        }
        
        return false;
    }
}