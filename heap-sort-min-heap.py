class MinHeap:
    def __init__(self, capacity):
        """
        Initializes a Min Heap with a given capacity.
        """
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def getParentIndex(self, index):
        return (index - 1) // 2

    def getLeftChildIndex(self, index):
        return 2 * index + 1

    def getRightChildIndex(self, index):
        return 2 * index + 2

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size

    def insert(self, value):
        """
        Inserts a new value into the Min Heap.
        """
        if self.size >= self.capacity:
            return "Heap is full"
        
        self.storage[self.size] = value
        self.size += 1
        self.heapifyUp()

    def heapifyUp(self):
        """
        Heapifies up to maintain the Min Heap property.
        """
        index = self.size - 1
        while self.hasParent(index) and self.storage[index] < self.storage[self.getParentIndex(index)]:
            self.storage[index], self.storage[self.getParentIndex(index)] = self.storage[self.getParentIndex(index)], self.storage[index]
            index = self.getParentIndex(index)

    def extractMin(self):
        """
        Extracts and returns the minimum element from the Min Heap.
        """
        if self.size == 0:
            return "Heap is empty"
        
        min_value = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDown()
        return min_value

    def heapifyDown(self):
        """
        Heapifies down to maintain the Min Heap property.
        """
        index = 0
        while self.hasLeftChild(index):
            smaller_child_index = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.storage[self.getRightChildIndex(index)] < self.storage[smaller_child_index]:
                smaller_child_index = self.getRightChildIndex(index)
            
            if self.storage[index] < self.storage[smaller_child_index]:
                break
            
            self.storage[index], self.storage[smaller_child_index] = self.storage[smaller_child_index], self.storage[index]
            index = smaller_child_index


# Test the Min Heap
min_heap = MinHeap(10)
min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(15)
min_heap.insert(1)

print("Min value:", min_heap.extractMin())  # Should print 1
print("Min value:", min_heap.extractMin())  # Should print 5
