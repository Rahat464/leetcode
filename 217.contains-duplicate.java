/*
 * @lc app=leetcode id=217 lang=java
 *
 * [217] Contains Duplicate
 */

// @lc code=start
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();

        for (Integer n: nums){
            if (seen.contains(n)){return true;}
            else {
                seen.add(n);
            }
        }

        return false;
    }
}
// @lc code=end

