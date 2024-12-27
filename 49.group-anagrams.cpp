/*
 * @lc app=leetcode id=49 lang=cpp
 *
 * [49] Group Anagrams
 */

// @lc code=start
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        unordered_map<string, vector<string>> map;

        for (string word : strs) {
            string key = word;
            sort(key.begin(), key.end());
            map[key].push_back(word);
        }

        for (const pair<const string, vector<string>>& pair : map) {
            result.push_back(pair.second);
        }

        return result;
    }
};
// @lc code=end

