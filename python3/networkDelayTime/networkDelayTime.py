'''
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

 

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
 

Note:
N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
'''


class Solution1:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # Implement using DFS

        # Assumptions:

        # Notes:
        # 0. Given a positive integer N input value which represents the number of network nodes. N > 0
        # 1. Given a list of travel times where times[i] = [u, v, w]
        # 2. Network nodes are connected as a directed graph
        # 3. Given a positive integer K which represents the starting node from where the signal is sent. K > 0
        # 4. Return the time it takes until all nodes recieve their signal from the starting node.
        # Return -1 if it is impossible

        # Time - O(T + N) | Space - O(N)
        graph = NetworkGraphDFS(times, N)

        # Time - O(E^2 + ELog(E)) | Space - O(E^2)
        graph.sendSignal(K, 0)

        # Time - O(N)
        ans = max(graph.distances.values())

        return ans if ans < float('inf') else -1


class NetworkGraphDFS:
    def __init__(self, times, N):
        self.graph = {}

        # Initialize node distance values to positive infinity to indicate that
        # the nodes have not been verified if there is a path to them from the K node.

        # Time - O(N) | Space - O(N)
        self.distances = {node: float('inf') for node in range(1, N+1)}

        # Time - O(T) | Space - O(N):
        self.connectNodes(times)

    # Time - O(T):
    # T represnts the length of times list.

    # Space - O(2N) -> O(N):
    # N represents the number of network nodes.
    # Worst case is our graph contains N amount of unique network nodes.
    # Also, each network node key can have up to (N-1) amount of nodes in it's adjaceny list (neighbors)

    def connectNodes(self, times):
        for sourceNode, targetNode, cost in times:
            self.graph[sourceNode] = self.graph.get(sourceNode, [])
            self.graph[sourceNode].append((cost, targetNode))

    # Time - O(E^2 + ELog(E))
    # Every edge node can be visited by all the other edge nodes.
    # The built in python sorted function used to sort the adjaceny neighbor list of a node takes O(E * log(E)) time.

    # Space - O(E^2):
    # With every edge node having the possibility to be visited by all the other edge nodes the
    # dfs recursion method is called on for however many times it is also visited therefore
    # it takes up O(E^2) space in our call stack frame.

    def sendSignal(self, node, elapsed):
        if elapsed >= self.distances[node]:
            return

        self.distances[node] = elapsed

        self.graph[node] = self.graph.get(node, [])

        for time, neighbor in sorted(self.graph[node]):
            self.sendSignal(neighbor, elapsed + time)


class Solution2:
    # Time - O(T + N^2) | Space - O(N)
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # Implement using Djikstra and BFS

        # Assumptions:

        # Notes:
        # 0. Given a positive integer N input value which represents the number of network nodes. N > 0
        # 1. Given a list of travel times where times[i] = [u, v, w]
        # 2. Network nodes are connected as a directed graph
        # 3. Given a positive integer K which represents the starting node from where the signal is sent. K > 0
        # 4. Return the time it takes until all nodes recieve their signal from the starting node.
        # Return -1 if it is impossible

        # Time - O(N) | Space - O(N)
        # N represents the total amount of n network nodes
        networkGraph = NetworkGraphDjikstra(N)

        # Time - O(T):
        # T represents the length of times array input
        # Space - O(N)
        networkGraph.connectNodes(times)

        # Time - O(N^2) | Space - O(N)
        # N represents the total amount of n network nodes
        networkGraph.sendSignal(K)

        # Time - O(N) | Space - O(N)
        ans = max(networkGraph.distances.values())

        return ans if ans < float('inf') else -1


class NetworkGraphDjikstra:
    # Time - O(2N) -> O(N)
    # Space - O(2N) -> O(N)
    def __init__(self, N):
        self.N = N
        self.graph = {}

        # Time - O(N) | Space - O(N)
        self.distances = {node: float('inf') for node in range(1, self.N+1)}

        # Time - O(N) | Space - O(N)
        self.seen = [False] * (self.N+1)

    # Time - O(T)
    # Space - O(N)
    # T represents the length of times array input

    # Tuple format ordered differently for djikstra; targetNode first then cost
    def connectNodes(self, times):
        # Time - O(T)
        # Space - O(2N) -> O(N)
        for sourceNode, targetNode, cost in times:
            self.graph[sourceNode] = self.graph.get(sourceNode, [])
            self.graph[sourceNode].append((targetNode, cost))

    # Time - O(N^2)
    # Space - O(N)
    # N represents the total amount of n network nodes
    def sendSignal(self, node):
        # Initialize K node with 0 value since it doesn't cost anything to reach itself.
        self.distances[node] = 0

        # Time - O(2N^2), if we remove constant -> O(N^2)
        # Until all nodes are visited, we iterate through all other nodes.
        # In other words, for every node we have to iterate through all other nodes.

        # Space - O(N - 1) -> O(N)
        # Worst case is we have to add a candidate node's neighbors as keys to our graph if they don't already exist.
        # This happens when a candidate node whose neighbors' node keys all don't exist in the graph,
        # we would have to add all the node keys with a default value of empty array in the graph.

        # Similar to topological sort?
        while True:
            cand_node = -1
            cand_dist = float('inf')

            # Time - O(N)
            for i in range(1, self.N+1):
                # Pick the next candidate node that we have not seen yet and also
                # has the smallest distance to travel?
                if not self.seen[i] and self.distances[i] < cand_dist:
                    cand_dist = self.distances[i]
                    cand_node = i

            # We break out if we've either already visited all nodes or
            # there is no path from K node to a particular node.
            if cand_node < 0:
                break

            self.seen[cand_node] = True

            self.graph[cand_node] = self.graph.get(cand_node, [])

            # Time - O(N)
            for neighbor, cost in self.graph[cand_node]:
                self.distances[neighbor] = min(
                    self.distances[neighbor], self.distances[cand_node] + cost)
