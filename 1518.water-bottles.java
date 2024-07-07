/*
 * @lc app=leetcode id=1518 lang=java
 *
 * [1518] Water Bottles
 */

// @lc code=start
class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int empty, res, exchanged;
        empty = res = numBottles;

        while (empty >= numExchange){
            exchanged = Math.floorDiv(empty, numExchange);
            res += exchanged;
            empty = exchanged + (empty % numExchange);
        };

        return res;
    }
}
// @lc code=end

