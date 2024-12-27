/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

// @lc code=start
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;

        for (int i = 0; i < nums.size(); i++) {
            const int n = nums[i];
            const int newTarget = target - n;
            
            if (map.find(newTarget) != map.end()) 
                return {map[newTarget], i};
            map[n] = i;
        }
        return {};
    }
};
// @lc code=end

