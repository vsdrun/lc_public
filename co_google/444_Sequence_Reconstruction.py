#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/sequence-reconstruction/description/

Check whether the original sequence org can be uniquely reconstructed from
the sequences in seqs.

The org sequence is a permutation of the integers from 1 to n,
with 1 ≤ n ≤ 104.

Reconstruction means building a shortest common supersequence of the
sequences in seqs
(i.e., a shortest sequence so that all sequences in seqs are
subsequences of it).

Determine whether there is only one sequence that can be
reconstructed from seqs and it is the org sequence.

Example 1:
Input:
org: [1,2,3], seqs: [[1,2],[1,3]]
Output:
false

Explanation:
[1,2,3] is not the only one sequence that can be reconstructed,
because [1,3,2] is also a valid sequence that can be reconstructed.



Example 2:
Input:
org: [1,2,3], seqs: [[1,2]]

Output:
false

Explanation:
The reconstructed sequence can only be [1,2].


Example 3:
Input:
org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]

Output:
true

Explanation:
The sequences [1,2], [1,3],
and [2,3] can uniquely reconstruct the original sequence [1,2,3].


Example 4:
Input:
org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]

Output:
true

explain:
https://leetcode.com/problems/sequence-reconstruction/discuss/92576/Understanding-the-problem

not toposort solution/idea:
https://leetcode.com/problems/sequence-reconstruction/discuss/92574/Very-short-solution-with-explanation

Use toposort to deal with this question.
"""


class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        """
        我的想法:
        Merge graph, 然後判斷此graph的toposort 是否唯一.

        a digraph has a unique topological ordering if and only if there is a
        (directed edge) between each pair of consecutive vertices in the
        topological order (i.e., the digraph has a Hamiltonian path).

        https://www.geeksforgeeks.org/strongly-connected-components/

        每個頭node的子node是否為一個SCC

        缺點 以上方法太慢...

        所以:
        改檢查 seqs裡的數 每一個seq其兩兩組成的順序是否符合
        org這個super sequence裡的組成順序.
        """
        # dict: Key: Value, Value: index

        # 只是用來看 seqs 裡的值是否後大於前 若是 則 False.
        index = {num: i for i, num in enumerate([None] + org)}

        pairs = set(zip([None] + org, org))

        for seq in seqs:
            for a, b in zip([None] + seq, seq):

                # 必須要有以下判斷! 因為...
                # 考慮seqs 有 [1,1] 重複的情況...
                if index[a] >= index.get(b, 0):
                    return False

                pairs.discard((a, b))

        return not pairs

    def rewrite(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """

        # 只是用來看 seqs 裡的值是否後大於前 若是 則 False.
        index = {num: i for i, num in enumerate([None] + org)}

        pairs = set(zip([None] + org, org))

        for seq in seqs:
            for a, b in zip([None] + seq, seq):

                print("a:{} b: {}".format(a, b))
                # 必須要有以下判斷! 因為...
                # 考慮seqs 有 [1,1] 重複的情況...
                # 並且 因為 [None] + seq, 所以 即使a out of index,
                # 也會成為 b, 因為 a 總是 None. 此時 , return False.
                if index[a] >= index.get(b, 0):
                    return False

                pairs.discard((a, b))

        return not pairs


def build():
    return [5, 3, 2, 4, 1], \
        [[5, 3, 2, 4], [4, 1], [1], [3], [2, 4], [1000000000, 99, 3]]
    return [1], [[1, 1]]
    return [1, 2, 3], [[1, 2], [1, 3]]
    return [1], [[1, 1]]
    return [4, 1, 5, 2, 6, 3], [[5, 2, 6, 3], [4, 1, 5, 2]]


if __name__ == "__main__":
    s = Solution()
    print(s.sequenceReconstruction(*build()))
    print(s.rewrite(*build()))
