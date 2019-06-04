#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/unique-word-abbreviation/


An abbreviation of a word follows the form <first letter><number><last letter>.
Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
     ↓
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
     ↓   ↓    ↓    ↓  ↓
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
     ↓   ↓    ↓
d) l|ocalizatio|n          --> l10n

Assume you have a dictionary and given a word,
find whether its abbreviation is unique in the dictionary.
A word's abbreviation is unique if no other word from the dictionary
has the same abbreviation.


Example:
Given dictionary = [ "deer", "door", "cake", "card" ]
isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true

"""


class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        dd = dictionary

        self.dset = dict()

        for d in dd:
            if d:
                if len(d) > 1:
                    self.dset[
                        d[0] + str(len(d[1:-1])
                                   if len(d[1:-1]) else "") + d[-1]] = d
                else:
                    self.dset[d] = d

        print(self.dset)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        d = word
        w = None

        if d:
            if len(d) > 1:
                w = d[0] + str(len(d[1:-1]) if len(d[1:-1]) else "") + d[-1]
        print("d: {}".format(d))
        print("w: {}".format(w))
        print("self.dset: {}".format(self.dset))
        if not w:
            w = d
        print("w: {}".format(w))

        if w in self.dset:
            if d in self.dset[w]:
                return False
            return False
        else:
            return True


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)

def build():
    return ["hello"]
    return ["deer", "door", "cake", "card"]
    return ["a", ""]
    return ["deer", "door", "cake", "card"]


if __name__ == "__main__":
    s = ValidWordAbbr(build())
    print(s.isUnique("hello"))
    print(s.isUnique("door"))
