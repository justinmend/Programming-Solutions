'''

  You're given a list of arbitrary jobs that need to be completed; these jobs
  are represented by distinct integers. You're also given a list of dependencies. A
  dependency is represented as a pair of jobs where the first job is a
  prerequisite of the second one. In other words, the second job depends on the
  first one; it can only be completed once the first job is completed.

  Write a function that takes in a list of jobs and a list of dependencies and
  returns a list containing a valid order in which the given jobs can be
  completed. If no such order exists, the function should return an empty array.
'''
# Time - O(J + 2D) -> O(J + D)
# Space - O(J + 2D) -> O(J + D)
def topologicalSort(jobs, deps):
	# Implement using Topological sort
	
    # Notes:
	# 0. Given a distinct integers for jobs array input.
	# 1. Return a list containing a valid order in which the given jobs can be completed.
	# 2. If no such order exists, return an empty array.
	
	# Time - O(J + D) | Space - O(J + D)
	# J represents the length of the jobs input
	# D represents the length of the deps list input.
	jobGraph = JobGraph(jobs, deps)
	
	# Time - O(D) | Space - O(D)
	# D represents the length of the deps list.
	return getOrderedJobs(jobGraph)

# Time - O(3D) -> O(D) | Space - O(3D) -> O(D)
# D represents the length of the deps list.
def getOrderedJobs(graph):
	orderedJobs = []
	
	# Time - O(D) | Space - O(D)
	# D represents the length of the deps list input.
	# Worst case is that in our deps list, all pairs we recieve where the first value in the pair (first job),
	# is not dependent on any job.
	# All those (first job) will have 0 value for its numOfPRereqs, thus, we could end up
	# adding as many nodes with the length of the deps list into our nodesWithNoPrereqs list. 
	nodesWithNoPrereqs = list(filter(lambda node: node.numOfPrereqs == 0, graph.nodes))
	
	# Time - O(P + A), P + A == D, therefore O(P + A) -> O(D)
	# D represents the length of the deps list input.
	# P represents the length of nodesWithNoPrereqs list.
	# A represents a node's deps adjaceny list
	# Worst case is P + A is equal to length of D
	
	# Space - O(P + A), P + A == D, therefore O(P + A) -> O(D)
	# D represents the length of the deps list input.
	# P represents the length of nodesWithNoPrereqs list.
	# A represents a node's deps adjaceny list
	# Worst case is P + A is equal to length of D
	# We are adding the total amount of nodes in nodesWithNoPrereqs into our orderedJobs list.
	
	# nodesWithNoPrereqs acts as our stack (LIFO)
	# We pop a node, look through its adjaceny list and add the nodes to nodeswithNoPrereqs
	# if they don't have any prereqs.
	while len(nodesWithNoPrereqs):
		node = nodesWithNoPrereqs.pop()
		orderedJobs.append(node.job)
		
		# Time - O(A) | Space - O(A)
		removeDeps(node, nodesWithNoPrereqs)
	
	# Time - O(D) | Space - O(D)
	graphHasEdges = any(node.numOfPrereqs for node in graph.nodes)
	return [] if graphHasEdges else orderedJobs

# Time - O(A):
# A represents a node's deps adjaceny list
# Worst case is that the current nodes' deps adjaceny list has all of its nodes
# with 0 numOfPrereqs.

# Space - O(A):
# Worst case is we would be adding the total amount of nodes into our nodesWithNoPrereqs list which is proportionate
# to the target node's deps list length which we are trying to remove all the other nodes dependent to it.
def removeDeps(node, nodesWithNoPrereqs):
	while len(node.deps):
		dep = node.deps.pop()
		dep.numOfPrereqs -= 1
		if dep.numOfPrereqs == 0:
			nodesWithNoPrereqs.append(dep)
	
class JobGraph:
	def __init__(self, jobs, deps):
		self.nodes = []
		self.graph = {}
		
		# Time - O(J) | Space - O(J)
		# J represents the length of the jobs input
		self.addJobs(jobs)
		
		# Time - O(D) | Space - O(D)
		# D represents the length of the deps list input.
		self.addDeps(deps)
	
	# Time - O(J) | Space - O(J)
	def addJobs(self, jobs):
		for job in jobs:
			self.addNode(job)
	
	def addNode(self, job):
			self.graph[job] = JobNode(job)
			self.nodes.append(self.graph[job])
	
	# Time - O(D) | Space - O(3D) -> O(D)
	# D represents the length of the deps list input.
	# Worst case is all the nodes we encounter in the 
	# deps list are not part of the jobs list.
	# We would then have to add those nodes into our graph.
	def addDeps(self, deps):
		for job, dep in deps:
			jobNode = self.getNode(job)
			depNode = self.getNode(dep)
			jobNode.deps.append(depNode)
			depNode.numOfPrereqs += 1
	
	def getNode(self, job):
		if job not in self.graph:
			self.addNode(job)
		
		return self.graph[job]


class JobNode:
	def __init__(self, job):
		self.job = job
		self.deps = []
		self.numOfPrereqs = 0
