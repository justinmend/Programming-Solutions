'''
We're going to make our own Contacts application! The application must perform two types of operations:

add name, where  is a string denoting a contact name. This must store  as a new contact in the application.
find partial, where  is a string denoting a partial name to search the application for. It must count the number of contacts starting with  and print the count on a new line.
Given  sequential add and find operations, perform each operation in order.

Input Format:
The first line contains a single integer, , denoting the number of operations to perform.
Each line  of the  subsequent lines contains an operation in one of the two forms defined above.

Constraints:
It is guaranteed that  and  contain lowercase English letters only.
The input doesn't have any duplicate  for the  operation.

Output Format:
For each find partial operation, print the number of contact names starting with  on a new line.

Sample Input:
4
add hack
add hackerrank
find hac
find hak

Sample Output:
2
0

Explanation:
We perform the following sequence of operations:
Add a contact named hack.
Add a contact named hackerrank.
Find and print the number of contact names beginning with hac. There are currently two contact names in the application and both of them start with hac, so we print  on a new line.
Find and print the number of contact names beginning with hak. There are currently two contact names in the application but neither of them start with hak, so we print  on a new line.
'''

#!/bin/python3

import os
import sys

#
# Complete the contacts function below.
#


def contacts(queries):
    # Assumptions:

    # Notes:
    # 1. Given a list of query commands perform each query. queries[i] >= 1
    # 2. The first query line contains a single integer n which represents the
    # number of operations to perform.
    # 3. Each line  of the  subsequent lines contains an operation in one of the
    # two forms defined above.

    # Brute Force:
    # Trie?

    trie = Trie()
    result = []

    for query in queries:
        if query[0] == 'add':
            trie.add(query[1])
        else:
            result.append(trie.findPartial(query[1]))

    return result


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Time - O(N) | Space - O(N)
    # N represents the length of the word we are trying to add to our trie.
    # Worst case is we are appending every character in the word to our trie
    # if the characters do not already exist in the trie.
    def add(self, word):
        curNode = self.root

        for ch in word:
            curNode.putChildIfAbsent(ch)
            curNode = curNode.getChild(ch)
            # Increment size for the current node. If there is an existing node for the current
            # character then we know there is more than one word sharing that same sequence of characters.
            # The node size property indicates how many words share that path of sequence of characters.
            curNode.size += 1

    # Time - O(P) | Space - O(1)
    # P represents the length of the partial we are trying to find in our trie.
    def findPartial(self, partial):
        curNode = self.root

        for ch in partial:
            curNode = curNode.getChild(ch)
            # return 0 automatically since the sequence of characters for the partial does not exist
            # in the trie.
            if curNode is None:
                return 0

        return curNode.size


class TrieNode:
    def __init__(self):
        self.children = {}
        self.size = 0

    def putChildIfAbsent(self, ch):
        if ch not in self.children:
            self.children[ch] = TrieNode()

    def getChild(self, ch):
        if ch in self.children:
            return self.children[ch]
        return None


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
