#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/find-the-duplicate-number/description/

Given an array nums containing n + 1 integers where each integer is
between 1 and n (inclusive),
prove that at least one duplicate number must exist.
Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

--------
An example to help understand.
suppose we have 5 integers: 1,3,1,4,2, and we start to jump from index:0

So the jumping sequence will be liked this: 1(jump to index 1) -> 3 (jump to index 3, so next is 4) -> 4 -> 2 -> 1 (formed a cycle here)
From this we can see the entry point of the cycle is the duplicated one.

Another Rho-shape example: 2,3,4,1,1
The jumping sequence will be liked this:
2 -> 4 ->1->3->1(formed a cycle here) : Non-cycle part is : 2->4 and cycle part is: 1->3
Again the entry point "1" is the duplicated number.

From now on we can follow the strategy of linked-list problem to solve it.

public int FindDuplicate(int[] nums)
{
        var slow = nums[0];
        // fast works same as slow but moves twice fast
        var fast = nums[0];
        fast = nums[fast];
        while(fast != slow){
            slow = nums[slow];
            // fast works same as slow but moves twice fast
            fast = nums[fast];
            fast = nums[fast];
        }
        fast = 0;
        while(fast != slow){
            slow = nums[slow];
            fast = nums[fast];
        }
        return fast;
}
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        2 pointers jump.
        """
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast= nums[nums[fast]]

        print("fast: {}".format(fast))
        print("slow: {}".format(slow))
        print("num: {}".format(nums[slow]))

        fast = 0
        while slow != fast:
            slow = nums[slow]
            print("slow: {}".format(slow))
            fast = nums[fast]

        return fast


    def rewrite(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Using xor.
        """
        xor = 0

        for n in nums:
            xor ^= n

        for i in range(1, len(nums) + 1):
            xor ^= i

        last = xor & -xor

        x = y = 0

        for i in range(len(nums)):
            if last & nums[i]:
                x ^= nums[i]
            else:
                y ^= nums[i]

        for i in range(1, len(nums) + 1):
            if i & last:
                x ^= i
            else:
                y ^= i

        return x if x in nums else y

def build():
    return [3,1,3,4,2]
    return [2,2,2,2,2]
    return [2,2]
    return [1,3,4,2,2]


if __name__ == "__main__":
    s = Solution()
    print(s.findDuplicate(build()))
