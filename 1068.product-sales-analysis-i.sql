--
-- @lc app=leetcode id=1068 lang=mysql
--
-- [1068] Product Sales Analysis I
--

-- @lc code=start
# Write your MySQL query statement below
SELECT
    p.product_name,
    s.year,
    s.price
FROM Sales s
INNER JOIN Product p USING (product_id);
-- @lc code=end

