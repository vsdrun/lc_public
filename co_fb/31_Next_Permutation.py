#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/next-permutation/description/

Implement next permutation, which rearranges numbers into the
lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest
possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its
corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1


void nextPermutation(vector<int>& nums) {
    auto i = is_sorted_until(nums.rbegin(), nums.rend());
    if (i != nums.rend())
        swap(*i, *upper_bound(nums.rbegin(), i, *i));
    reverse(nums.rbegin(), i);
}
"""


class Solution(object):
    def nextPermutation(self, num):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not num:
            return

        """
        1. 由後往前排序有小到大.
        2. 例: 2 9 4 3 1 , 到2為止. 則將2與之前排序中第一個比2大的交換:
             3 9 4 2 1,
        3. 再將9 4 2 1小到大排序: 3 1 2 4 9
        """
        from __builtin__ import xrange
        count = 0

        for i in xrange(num.__len__() - 1, -1, -1):
            if i == 0:
                if count == (num.__len__() - 1):
                    num[:] = sorted(num)
                    break

            if num[i] > num[i-1]:
                num[i:] = sorted(num[i:])
                for inx, tval in enumerate(num[i:]):
                    tinx = inx + i
                    if tval > num[i-1]:
                        """Swap"""
                        num[i-1], num[tinx] = tval, num[i-1]
                        break
                break
            else:
                count += 1

        return num

    def rewrite(self, num):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def bisect(n, item):
            """
            n is inverse sorted list.
            含       不含
            [9,4,2,2,1]

            [3], 2
            """
            item += 1  # because we are asking for larger then the item.
            tail= len(n)
            head = 0

            while True:
                mid = head + (tail - head)/2

                if mid == head:
                    return mid

                if item > n[mid]:
                    tail = mid
                else:
                    head = mid

        def reverse(head, tail):
            while head < tail:
                num[head] , num[tail] = num[tail], num[head]
                head += 1
                tail -= 1


        hit = False

        #  [2, 9, 1, 2, 3] # 3 9 1 2 2
        for idx in range(len(num) - 2, -1, -1):
            if num[idx] >= num[idx + 1]:
                continue

            hit = True

            current_small = num[idx]
            # find the one before which is large then current_small
            #  cidx = bi.bisect_right(num[idx + 1:], current_small) + idx + 1

            cidx = bisect(num[idx + 1:], current_small)

            cidx = cidx + 1 + idx

            num[cidx], num[idx] = num[idx], num[cidx]


            # reverse sort the rest
            head = idx + 1
            tail = len(num) - 1
            reverse(head, tail)
            break

        if not hit:
            head = 0
            tail = len(num) - 1
            reverse(head, tail)

    def rewrite2(self, num):
        """
        Best solution :-)
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        import bisect as bi

        for idx in range(len(num) - 1, -1, -1):
            if idx == 0:
                num.sort()
                return

            if num[idx - 1] < num[idx]:
                #  [1, 1, 5]
                rnum = num[idx:][::-1]

                nlidx = bi.bisect_right(rnum, num[idx - 1])
                nv = rnum[nlidx]
                # beware of duplicate value
                nidx = num[idx:].index(nv) + idx

                num[idx - 1], num[nidx] = num[nidx], num[idx - 1]
                num[idx:] = sorted(num[idx:])
                return


def build():
    return [1, 1, 5]
    return [3, 4, 9, 5, 2, 1]
    return [2, 9, 1, 2, 3] # 3 9 1 2 2
    return [1, 2, 3]
    return [3, 2, 1]
    return [5,4,7,5,3,2]
    return [9, 2, 1]
    return [2, 9, 3, 2, 1]


if __name__ == "__main__":

    s = Solution()
    n = build()
    s.nextPermutation(n)
    print(n)

    n = build()
    s.rewrite(n)
    print(n)

    n = build()
    s.rewrite2(n)
    print(n)
