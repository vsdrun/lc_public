#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/top-k-frequent-elements/description/

Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
***
Your algorithm's time complexity must be better than O(n log n),
where n is the array's size.
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections as cc

        cnt = cc.Counter(nums)

        result = []
        lk = 0
        # most_common return list of tuple (val, cnt)
        mc = cnt.most_common()

        while lk < k:
            result.append(mc[lk][0])
            lk += 1
        return result

    def rewrite(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        # bucket sort
        return zip(*collections.Counter(nums).most_common(k))[0]

    def rewrite2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict as dd
        dmap = dd(int)

        for n in nums:
            dmap[n] += 1

        reverseDmap = dd(list)

        for key, val in dmap.iteritems():
            reverseDmap[val].append(key)

        result = []
        for key in sorted(reverseDmap.keys(), reverse=True):
            if k == 0:
                break
            for v in reverseDmap[key]:
                if k != 0:
                    result.append(v)
                    k -= 1
                else:
                    break

        return result

    def rewrite3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        import heapq as hq
        from collections import defaultdict as dd

        dmap = dd(int)
        result = []

        for n in nums:
            dmap[n] += 1
            hq.heappush(result, (-dmap[n], n))

        kset = set()
        kresult = []

        while k > 0:
            _, val = hq.heappop(result)
            if val in kset:
                continue

            kset.add(val)
            kresult.append(val)
            k -= 1

        return kresult


def build():
    return [1,1,1,2,2,3], 2
    return [1], 1
    return [5,3,1,1,1,3,73,1], 2


if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent(*build()))
    print(s.rewrite(*build()))
    print(s.rewrite2(*build()))
    print(s.rewrite3(*build()))
