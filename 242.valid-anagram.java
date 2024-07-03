/*
 * @lc app=leetcode id=242 lang=java
 *
 * [242] Valid Anagram
 */

// @lc code=start
class Solution {
    public boolean isAnagram(String s, String t) {
        // Check if they're both the same length
        if (s.length() != t.length()) return false;

        // Count freq of each letter in word
        int[] freq = new int[26];

        // Count characters in s
        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }
        // Check if s has matching number of characters
        for (char c : t.toCharArray()){
            if (freq[c - 'a'] < 1){
                return false;
            }
            freq[c - 'a']--;
        }

        return true;
    }
}
// @lc code=end

