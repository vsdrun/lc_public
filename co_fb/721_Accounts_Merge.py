#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/accounts-merge/description/

Given a list accounts, each element accounts[i] is a list of strings,
where the first element accounts[i][0] is a name,
and the rest of the elements are emails representing emails of the account.

a[0]=name
a[...]=emails

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
        my best solution.

        1. 名字會重複 所以不能當unique key, 故我們以enumerate count作為unique
        key
        """
        from collections import defaultdict as dd

        # email: account number
        dmap = dd(list)
        result = []

        for acct, value in enumerate(accounts):
            for email in value[1:]:
                dmap[email].append(acct)


        visited = set()
        emailed = set()

        def dfs(email):
            """
            :ret: emails
            """
            emails = [email]

            for acnt in dmap[email]:
                if acnt in visited:
                    continue

                visited.add(acnt)

                for e in accounts[acnt][1:]:
                    if e in emailed:
                        continue
                    emailed.add(e)
                    emails.extend(dfs(e))

            return emails


        for accnt, val in enumerate(accounts):
            if accnt in visited:
                continue

            visited.add(accnt)
            result.append([val[0]])

            for email in val[1:]:
                if email in emailed:
                    continue
                emailed.add(email)
                result[-1].extend(dfs(email))

            result[-1][1:] = sorted(result[-1][1:])

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
    print(s.accountsMerge(build()))
