# Time - O(Nlog(N)) | Space - O(N)
# Bounded by the built in python3 sorted function (tim sort algorithm)


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # map word by frequency
        # sort by frequency
        # use lambda to handle ties

        # Time - O(N) | Space - O(N)
        my_dict = collections.Counter(words)

        # When a dictionary is sorted using python3 sorted, it defaults
        # to use the dictionary keys for the lambda sorting.

        # Time - O(Nlog(N)) | Space - O(N)
        result = sorted(my_dict, key=lambda word: (-my_dict[word], word))

        # Another way which is more straight forward and clear is to directly use the keys
        # result = sorted(my_dict.keys(), key=lambda word: (-my_dict[word], word))

        return result[:k]
