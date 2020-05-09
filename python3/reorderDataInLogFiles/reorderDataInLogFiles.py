# Time - O(Nlog(N)) | Space - O(N)
# Tim sort algorithm takes O(Nlog(N)) time


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs = []
        digitLogs = []

        # Time - O(N x S) | Space - O(N)
        for log in logs:

            if log.split()[1].isalpha():
                letterLogs.append(log)
            else:
                digitLogs.append(log)

        # sort
        # use lambda
        # Time - O(2 * Nlog(N)) | Space - O(N)
        letterLogs.sort(key=lambda log: log.split()[0])
        letterLogs.sort(key=lambda log: log.split()[1:])

        # Time - O(N) | Space - O(N)
        return letterLogs + digitLogs
