#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/design-tinyurl/discuss/100258

https://leetcode.com/problems/design-tinyurl/description/

How would you design a URL shortening service that is similar to TinyURL?

Background:
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Requirements:
For instance, "http://tinyurl.com/4e9iAk" is the tiny url for the page "https://leetcode.com/problems/design-tinyurl". The identifier (the highlighted part) can be any string with 6 alphanumeric characters containing 0-9, a-z, A-Z.

Each shortened URL must be unique; that is, no two different URLs can be shortened to the same URL.

Note about Questions:
Below are just a small subset of questions to get you started. In real world, there could be many follow ups and questions possible and the discussion is open-ended (No one true or correct way to solve a problem). If you have more ideas or questions, please ask in Discuss and we may compile it here!


Questions:
How many unique identifiers possible? Will you run out of unique URLs?
Should the identifier be increment or not? Which is easier to design? Pros and cons?
Mapping an identifier to an URL and its reversal - Does this problem ring a bell to you?
How do you store the URLs? Does a simple flat file database work?
What is the bottleneck of the system? Is it read-heavy or write-heavy?
Estimate the maximum number of URLs a single machine can store.
Estimate the maximum number of queries per second (QPS) for decoding a shortened URL in a single machine.
How would you scale the service? For example, a viral link which is shared in social media could result in a peak QPS at a moment's notice.
How could you handle redundancy? i,e, if a server is down, how could you ensure the service is still operational?
Keep URLs forever or prune, pros/cons? How we do pruning? (Contributed by @alex_svetkin)
What API would you provide to a third-party developer? (Contributed by @alex_svetkin)
If you can enable caching, what would you cache and what's the expiry time?
"""

"""
S: Scenario
N: Need (Assume the system is not massive if you are not sure)

QPS (queries per second)
Storage

A: API
Only one service: URLService
Core (Business Logic) Layer:
    Class: URLService
Interface:
    URLService.encode(String long_url)
    URLService.decode(String short_url)
Web Layer:
REST API:
    GET: /{short_url}, return a http redirect response(301)
    POST: goo.gl method - google shorten URL


K: Data Access

Step 1: Pick a storage structure
SQL vs NoSQL?
Does it need to support transactions? NoSQL does not support transaction.
Do we need rich SQL query? NoSQL does not support as many queries as SQL.

Pursue development efficiency? Most Web Framework supports SQL database very well (with ORM). It means fewer codes for the system.

Do we need to use AUTO_INCREMENT ID? NoSQL couldn’t do this. It only has a global unique Object\_id.

Does the system has a high requirement for QPS? NoSQL has high performance. For example, Memcached’s QPS could reach million level, MondoDB does 10K level, MySQL only supports K level.

How high is the system’s scalability? SQL requires developers write their codes
to scale, while NoSQL comes with them (sharding, replica).




"""


def build():
    return [100, 4, 200, 1, 3, 2]


if __name__ == "__main__":
    nums = build()
