/*
 * @lc app=leetcode id=242 lang=cpp
 *
 * [242] Valid Anagram
 */

// @lc code=start
#include <string>;
#include <unordered_map>;
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        
        unordered_map<char, int> frequency;
        for (char c : s) frequency[c]++;
        for (char c : t){
            if (frequency.find(c) == frequency.end()) return false;
            frequency[c]--;
            if (frequency[c] == 0) frequency.erase(c);
        }
        return frequency.empty();
    }
};
// @lc code=end

