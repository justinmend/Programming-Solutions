'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 

Constraints:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
'''

class Solution:
    # Time - O(N^2) | Space - O(N^2):
    # W have to try every course in numCourses as a starting point when we try to find
    # a cycle in the graph.
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Implement using Topological Sort and DFS
        
        # Assumptions:
        # 1. numCourses > 0? Yes
        # 2. prerequisite pair values >= 0? Yes
        # 3. No duplicate edges in the input prerequesites, that is, no duplicate pair values.
        
        # Notes:
        # 1. Given an integer value representing the number of courses. numCourses > 0
        # 2. Given a list of prerequisite pairs. EX: [1, 2]
        # 3. Return boolean whether it is possible to finish all courses, that is, there is no cycle.
        # 4. numCourses is zero based index
        
        # Brute Force:
        # Creat a graph object
        # Add all courses as keys with their values an empty array.
        courseGraph = CourseGraph(numCourses)
        
        # Add all edges(dependencies) to the courses.
        courseGraph.addDependencies(prerequisites)
        
        # Create dfs helper method which detects if there is a cycle in the graph?
        # Call containsCycle method for each course
        # Pass in the course key
        # If containsCycle returns true, return False immediately
        
        # Time - O(N^2) | Space - O(N^2)
        for i in range(numCourses):
            if courseGraph.containsCycle(i):
                return False
        
        # Return true since we didn't encounter any cycle
        return True

class CourseGraph:
    # Time - O(N):
    # N represents the value of numCourses.
    # Space - O(N):
    # We create N total amount of keys in the graph.
    def __init__(self, numCourses):
        self.numCourses = numCourses
        self.graph = {}
        
        # How do we keep track of visited courses to make sure there is no cycle in the graph?
        # Create a boolean array with the length of numCourses
        self.visited = [False] * numCourses
        
        # Add all courses as keys with their values an empty array.
        for i in range(self.numCourses):
            self.graph[i] = []
    
    # Time - O(P):
    # P represents the total pairs in prerequisites array input.
    
    # Space - O(N):
    # N represents the value of numCourses.
    # At most, each course can only contain in its dependency list N amount of courses
    # since there are only up to N possible courses.
    def addDependencies(self, prereqs):
        # Iterate through the list of prerequisite pairs:
        # Add all edges(dependencies) to the courses.
        for prereq in prereqs:
            dep = prereq[0]
            course = prereq[1]
            self.graph[course].append(dep)
    
    # Time - O(N):
    # N represents the value of numCourses input.
    # We iterate in a depth first search fashion and we track of courses we already visit.
    # We have our base case to make sure we only visit a course once, that is, we make sure there
    # is no cycle. Thus, worst case is we only visit each course in numCourses once.
    
    # Space - O(N):
    # N represents the value of numCourses input.
    # At most we make a total of N recursion calls which takes up space in the call stack frame.
    def containsCycle(self, course):
        # Base Case:
        if self.visited[course]:
            return True

        # Set visited to true for current course
        self.visited[course] = True
        
        # Iterate through all the graph keys (course):
            # Go depth first for each depency of the current course.
            # Call recursion
        
        for dep in self.graph[course]:
            if self.containsCycle(dep):
                return True
        
        self.visited[course] = False