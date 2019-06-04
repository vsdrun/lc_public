#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/factor-combinations/description/


Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.

Write a function that takes an integer n and return all
possible combinations of its factors.

Note:
You may assume that n is always positive.
Factors should be greater than 1 and less than n.


Examples:
input: 1
output:
[]

input: 37
output:
[]

input: 12
output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]

input: 32
output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]

ref:
    http://www.cnblogs.com/grandyang/p/5332722.html

class Solution {
public:
    vector<vector<int>> getFactors(int n) {
        vector<vector<int>> res;
        helper(n, 2, {}, res);
        return res;
    }
    void helper(int n, int start, vector<int> out, vector<vector<int>> &res) {
        if (n == 1) {
            if (out.size() > 1) res.push_back(out);
        } else {
            for (int i = start; i <= n; ++i) {
                if (n % i == 0) {
                    out.push_back(i);
                    helper(n / i, i, out, res);
                    out.pop_back();
                }
            }
        }
    }
};


class Solution {
public:
    vector<vector<int>> getFactors(int n) {
        vector<vector<int>> res;
        helper(n, 2, {}, res);
        return res;
    }
    void helper(int n, int start, vector<int> out, vector<vector<int>> &res) {
        for (int i = start; i <= sqrt(n); ++i) {
            if (n % i == 0) {
                vector<int> new_out = out;
                new_out.push_back(i);
                helper(n / i, i, new_out, res);
                new_out.push_back(n / i);
                res.push_back(new_out);
            }
        }
    }
};


-------------------------------------
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
class Solution {
public:
    vector<vector<int>> getFactors(int n) {
        vector<vector<int>> res;

        for (int i = 2; i * i <= n; ++i) {
            if (n % i == 0) {

                vector<vector<int>> v = getFactors(n / i);
                vector<int> out{i, n / i};
                res.push_back(out);

                for (auto a : v) {
                    if (i <= a[0]) {
                        a.insert(a.begin(), i);
                        res.push_back(a);
                    }
                }
            }
        }

        return res;
    }
};
"""

class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        一層耗盡一個數的概念
        2, 2, 2... 3... 4...
        避免2,3,2的出現 只有2,2,3
        """
        def factor(n, i, combi, combis):
            while i * i <= n:
                if n % i == 0:
                    combis += combi + [i, n/i],

                    factor(n/i, i, combi+[i], combis)
                i += 1

            return combis

        return factor(n, 2, [], [])


def build(cnt):
    return 12


if __name__ == "__main__":

    s = Solution()
    print(s.getFactors(build()))
