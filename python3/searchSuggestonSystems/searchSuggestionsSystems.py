# Time - O(N * (L + log(N)) + S) | Space - O(N * L + S):
# N represents the length of the products list
# L represents the longest product string in the products list


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Use a trie?
        # At most, a list contains three product suggestions.

        # Sort the products lists
        # Time - O(Nlog(N)) | Space - O(N)
        # N represents the length of the products list
        # Python built in sorting function uses tim sort algorithm which takes O(Nlog(N)) time and O(N) space.
        products.sort()

        # Create trie:
        root = TrieNode()

        # Time - O(N * L) | Space - O(N * L * K) -> O(N * L):
        # N represents the length of the products list
        # L represents the longest product string in the products list
        # K represents the maximum amount of product suggestion as each character is typed but we can
        # remove it assuming it is constant.

        # Iterate through the products list
        for product in products:
            curNode = root
            # Iterate through each character of the product:
            for letter in product:
                # Add a key and default trie node if it doesn't exist yet.
                # Also, Move pointer to the list of children of the current node.
                curNode = curNode.children[letter]
                # Add the current product to the current trie node's suggestion list
                # Use a setter method, should only add if list is less than 3.
                curNode.addSuggestion(product)

        result = []
        curNode = root

        # Time - O(S) | Space - O(S):
        # S represents the length of the searchWord string
        # Iterate through each character of searchWord:
        for letter in searchWord:
            # Move pointer to list of children of the node with the character value
            curNode = curNode.children[letter]
            # Add the pointer node's suggestion list to the result list
            result.append(curNode.suggestions)

        # Return a list of lists
        return result


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.suggestions = []

    def addSuggestion(self, product):
        if len(self.suggestions) < 3:
            self.suggestions.append(product)
