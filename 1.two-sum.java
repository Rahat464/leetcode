/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 */

// @lc code=start
// import java.util.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] res = new int[2];

        for (int i=0;i<nums.length;i++){
            if (!map.containsKey(target-nums[i])) map.put(nums[i], i);
            else {
                res[1] = i;
                res[0] = map.get(target-nums[i]);
                return res;
            }
        }
        return null;

    }
}
// @lc code=end

