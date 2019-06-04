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

    def rewrite2(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        from collections import defaultdict as dd

        dmap = dd(list)
        # emails: accnt num
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

            emails.sort()
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

            result[-1].sort()


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
    print(s.rewrite2(build()))
