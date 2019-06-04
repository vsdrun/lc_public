#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/encode-and-decode-tinyurl/

Note: This is a companion problem to the System Design problem: Design TinyURL.

TinyURL is a URL shortening service where you enter a URL such
as https://leetcode.com/problems/design-tinyurl and it
returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service.
There is no restriction on how your encode/decode algorithm should work.
You just need to ensure that a URL can be encoded to a tiny URL
and the tiny URL can be decoded to the original URL.
"""
import random
import string


class Codec:
    # 聰明的作法
    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        """
        Only 6 chars for shorten url.
        If collision, regenerate again.
        """
        while longUrl not in self.url2code:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return 'http://tinyurl.com/' + self.url2code[longUrl]

    def decode(self, shortUrl):
        return self.code2url[shortUrl[-6:]]


if __name__ == "__main__":
    c = Codec()
    c.encode("http://haha")
    c.decode("pica")
