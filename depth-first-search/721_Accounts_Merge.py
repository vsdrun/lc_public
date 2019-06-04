#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/accounts-merge/description/

Given a list accounts, each element accounts[i] is a list of strings,
where the first element accounts[i][0] is a name,
and the rest of the elements are emails representing emails of the account.


Now, we would like to merge these accounts.
Two accounts definitely belong to the same person if there is some
email that is common to both accounts.


Note that even if two accounts have the same name,
they may belong to different people as people could have the same name.


A person can have any number of accounts initially,
but all of their accounts definitely have the same name.


After merging the accounts, return the accounts in the following format:
the first element of each account is the name,
and the rest of the elements are emails in **sorted order.
The accounts themselves can be returned in any order.



Example 1:
Input:
accounts =
[["John", "johnsmith@mail.com", "john00@mail.com"],
["John", "johnnybravo@mail.com"],
["John", "johnsmith@mail.com", "john_newyork@mail.com"],
["Mary", "mary@mail.com"]]

Output:
[["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
["John", "johnnybravo@mail.com"],
["Mary", "mary@mail.com"]]

Explanation:
The first and third John's are the same person as they have
the common email "johnsmith@mail.com".

The second John and Mary are different people as none of
their email addresses are used by other accounts.

We could return these lists in any order, for example the answer
[['Mary', 'mary@mail.com'],
['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']]

would still be accepted.


以email為key map 到account number.
DFS.
"""


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        import collections as cc

        mapping = cc.defaultdict(set)

        vistied = set()

        total_result = []

        # m[email] = name
        for act_num, row in enumerate(accounts):
            for email in row[1:]:
                mapping[email].add(act_num)

        def dfs(act_num, result):
            if act_num in vistied:
                return

            vistied.add(act_num)
            data = accounts[act_num]

            for email in data[1:]:
                result.add(email)

                for act in mapping[email]:
                    dfs(act, result)

        for act_num, row in enumerate(accounts):
            result = set()
            dfs(act_num, result)

            if result:
                total_result.append([row[0]] + sorted(result))

        return total_result

    def rewrite(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        """
        利用input data structure as map.
        """
        email_to_acnt_map = dict()

        # build graph
        for acntNo, data in enumerate(accounts):
            for email in data[1:]:
                if not email_to_acnt_map.get(email):
                    email_to_acnt_map[email] = set()
                email_to_acnt_map[email].add(acntNo)

        def dfs(acnt, result):
            if acnt in visited:
                return

            visited.add(acnt)

            data = accounts[acnt]

            for email in data[1:]:
                result.add(email)

                for next_acnt in email_to_acnt_map[email]:
                    dfs(next_acnt, result)

        visited = set()
        final_result = []

        for acntNo, data in enumerate(accounts):

            result = set()
            dfs(acntNo, result)

            if result:
                final_result.append([data[0]] + (sorted(result)))

        return final_result

    def rewrite2(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        """
        利用input data structure as map.
        """
        from collections import defaultdict as dd
        edmap = dd(set)

        [edmap[email].add(actNum) for actNum, l in enumerate(accounts)
            for email in l[1:]]

        def dfs(actNum, email):
            result = []

            actNums = edmap.pop(email, [])

            if actNums:
                result.append(email)

            for ac in actNums:
                if ac == actNum:
                    continue

                for e in accounts[ac][1:]:
                    result.extend(dfs(ac, e))

            return result

        result = []

        for actNum, l in enumerate(accounts):
            # 先為empty 方便之後做判斷.
            lresult = []

            for email in l[1:]:
                lresult.extend(dfs(actNum, email))

            if lresult:
                result.append([l[0]] + sorted(lresult))

        return result


def build():
    return [["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]]
    return [["John", "johnsmith@mail.com", "john00@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["Mary", "mary@mail.com"]]


if __name__ == "__main__":
    s = Solution()
    #  print(s.accountsMerge(build()))
    print(s.rewrite(build()))
    print(s.rewrite2(build()))
