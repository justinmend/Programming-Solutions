'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:
int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8

Note:
You may assume that nums' length ≥ k-1 and k ≥ 1.
'''


# For the purpose of this exercise, implement your own min heap priority queue using array format instead of binary tree.

# Assumptions:
# 1. You may assume that nums' length ≥ k-1 and k ≥ 1.
# 2. Can I modify nums input? Can I sort nums input in place?

# Notes:
# Heap property: Every parent's value must be less than it's childrens' value.

# Get child index formula:
# Left: 2i + 1
# Right: 2i + 2

# Get parent index formula:
# (i-1)/2

class KthLargest:
    
    # Initialization:
    # Use a min heap and keep it to a size of k.
    # Build the priority queue heap using a new list.
    # Iterate through the nums list and add into pq list.
    
    # Time Complexity - O(N*log(M)):
    # N represents the length of nums list. We iterate through the nums list once.
    # M represents the length of pq. We call the add function N times which uses bubble Up method that is O(log(M)) time.
    # Space Complexity - O(1):
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = []
        
        # How do we initialze pq in heap array format?
        for num in nums:
            self.add(num)
    
    # Add the new item first to the queue then check if the size is greater than k.
    # If so, pop off an item from the queue to keep k size.
    # Return the top of the item value in the pq list
    
    # Time Complexity - O(log(N)):
    # Space Complexity - O(1):
    def add(self, val: int) -> int:
        '''
            # Commented out. This is using python built in min heap functionality.
            heapq.heappush(self.pq,val)
            while len(self.pq) > self.k:
                heapq.heappop(self.pq)
        '''
        
        # Add element to end of pq list.
        # Use bubble up on last last element to satisfy heap property.
        # Keep track of pq size.
        # Keep removing items until pq is of size k.
        # Use self.remove() to remove the top item in min heap priority queue.
        
        self.pq.append(val)
        self.bubbleUp(len(self.pq)-1)
        
        while len(self.pq) > self.k:
            self.remove()
            
        return self.pq[0]

        
    # Bubble up:
    # Create parentIndx variable and use parent formula to get value.
    
    # Time Complexity - O(log(N)):
    # N represents the length of the min heap priority queue array.
    # The amount of items we only traversed through is cut in half
    # every time we go up to the parent item at the next level. We only traverse through
    # one item which is the parent item at each level we go to.
    # Space Complexity - O(1):
    # We only use auxiliary space for the bubble up method.
    def bubbleUp(self, curIdx):
        parentIdx = (curIdx - 1)//2
        
        while curIdx > 0:
            if self.pq[curIdx] < self.pq[parentIdx]:
                self.swap(curIdx, parentIdx)
                curIdx = parentIdx
                parentIdx = (curIdx - 1)//2
            else:
                break
    
    # Bubble down:
    # Create a leftChildIndx variable and use left child formula to get value.  
    
    # Time Complexity - O(log(N)):
    # N represents the length of the min heap priority queue array.
    # The amount of items we only traversed through is cut in half
    # every time we go down to the child item to at the next level. We only traverse through
    # one item which is either the left or right child item at each level.
    # Space Complexity - O(1):
    # We only use auxiliary space for the bubble down method.
    def bubbleDown(self, curIdx):
        leftChildIdx = (2*curIdx) + 1
        
        while leftChildIdx < len(self.pq):
            rightChildIdx = (2*curIdx) + 2
            
            if rightChildIdx > len(self.pq) - 1:
                if self.pq[curIdx] > self.pq[leftChildIdx]:
                    self.swap(curIdx, leftChildIdx)
                    curIdx = leftChildIdx
                else:
                    break
            else: 
                if self.pq[leftChildIdx] <= self.pq[rightChildIdx] and self.pq[leftChildIdx] < self.pq[curIdx]:
                    self.swap(leftChildIdx, curIdx)
                    curIdx = leftChildIdx
                elif self.pq[rightChildIdx] < self.pq[leftChildIdx] and self.pq[rightChildIdx] < self.pq[curIdx]:
                    self.swap(rightChildIdx, curIdx)
                    curIdx = rightChildIdx
                else:
                    break

            leftChildIdx = (2*curIdx) + 1
    
    # Remove:
    # Remove the top element from the heap array.
    # Swap the top item value with the end item value. Use swap method.
    # Remove the last item in heap array by popping of item.
    # We will want to call bubble down on the root (first item in array) to make sure heap property is fullfilled.
    
    # Time Complexity - O(log(N)):
    # Space Complexity - O(1):
    def remove(self):
        if len(self.pq) == 1:
            self.pq.pop()
        elif len(self.pq) > 1:
            self.swap(0, len(self.pq) - 1)
            self.pq.pop()
            self.bubbleDown(0)
    
    # Swap:
    def swap(self, swapIdx1, swapIdx2):
        self.pq[swapIdx1], self.pq[swapIdx2] = self.pq[swapIdx2], self.pq[swapIdx1]
    
    


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)