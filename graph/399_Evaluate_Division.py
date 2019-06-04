#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/evaluate-division/description/

Equations are given in the format A / B = k,
where A and B are variables represented as strings,
and k is a real number (floating point number).
Given some queries, return the answers.
If the answer does not exist, return -1.0.


Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].


The input is:
vector<pair<string, string>> equations, vector<double>& values,
vector<pair<string, string>> queries ,
where equations.size() == values.size(), and the values are positive.
This represents the equations. Return vector<double>.


According to the example above:
equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].

The input is always valid.
You may assume that evaluating the queries will result in
no division by zero and there is no contradiction.

Simple:
    a/b * b/c = a/c

    b/c * c/a = b/a
"""


class Solution(object):

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        import collections as cc

        # 用 dict 來建立graph.
        eqv = cc.defaultdict(list)

        # list of [(["a","b"],value]),...]
        # zip returns list of tuples
        eqz = zip(equations, values)

        # 重要! build 2-ways direct graph
        for (n, d), v in eqz:  # variable 在前 value在後 方便index.
            eqv[n] += (d, v),  # d * v
            eqv[d] += (n, 1 / v),  # n * 1/v

        result = []

        def dfs(no, deno, visited):

            for n, v in eqv[no]:
                if n in visited:
                    # c/a = ?
                    # if c = b / d, b = c / a, 則loop 應避免.
                    continue

                visited.add(n)

                if n == deno:
                    return v

                result = dfs(n, deno, visited)

                if result != -1.0:  # 止.
                    return v * result

            return -1.0  # 代表沒有答案.

        for n, d in queries:
            if n in eqv and n == d:
                result.append(1.0)
                continue

            # beware not to revisited causing endless loop.
            # 記得graph必須有visited set.
            visited = set()
            visited.add(n)
            result.append(dfs(n, d, visited))

        return result

    def rewrite(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        """
        Graph problem:
            a -> b (3)  b -> a (1/3)
            b -> c (2)  c -> b (1/2)
        路徑相乘即是答案.
        """
        eqq = equations
        vv = values
        qq = queries

        if not eqq or not vv or len(eqq) != len(vv) or not qq:
            return []

        # build graph

        from collections import defaultdict as dd

        dmap = dd(list)

        for _eq, _v in zip(equations, values):
            dmap[_eq[0]].append([_eq[1], _v])
            dmap[_eq[1]].append([_eq[0], 1.0/_v])

        def calx(nom, denom, v):
            if nom == denom and nom in dmap:
                return 1.0

            if nom not in dmap or denom not in dmap:
                return -1.0

            if nom in v:
                return -1.0

            v.add(nom)

            for val in dmap[nom]:
                next_denom = val[0]
                next_value = val[1]
                n_v = calx(next_denom, denom, v)

                if n_v != -1:
                    return next_value * n_v

            return -1
        result = []

        for q in qq:
            visited = set()
            result.append(calx(q[0], q[1], visited))

        return result


def build():
    return [["a", "b"], ["b", "c"]], [2.0, 3.0], \
        [["a", "c"], ["b", "a"],
         ["a", "e"], ["a", "a"], ["x", "x"]]

    return [["a", "b"], ["b", "c"]], [2.0, 3.0], \
        [["a", "c"], ["b", "c"], ["a", "e"], ["a", "a"], ["x", "x"]]


if __name__ == "__main__":
    e, v, q = build()

    s = Solution()
    result = s.calcEquation(e, v, q)
    print(result)

    result = s.rewrite(e, v, q)
    print(result)
