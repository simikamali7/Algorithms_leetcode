class MaxHeap:
    # A pointer pointing to the elements
    # in the array in the heap.
    arr = []
 
    # Maximum possible size of
    # the Max Heap.
    maxSize = 0
 
    # Number of elements in the
    # Max heap currently.
    heapSize = 0
 
    # Constructor function.
    # self.arr = a list of None (null) objects * maxSize
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.arr = [None]*maxSize
        self.heapSize = 0
 




    # Heapifies a sub-tree taking the given index as the root.
    # sets i (the index/root) as largest


    # in a binary heap data structure, the number of elements in the heap may be less than the
    # size of the underlying array that represents the heap. 
    # In such cases, the heap is said to have a "heap size" that is smaller than the "array size".


    # If l is less than self.heapSize, it means that the left child node exists in 
    # the heap and its index is valid. Therefore, the condition self.arr[l] > self.arr[i] can be checked 
    # to compare the value of the parent node at index i with the value of the left child node at index l.

    # If l is greater than or equal to self.heapSize, 
    # it means that the left child node does not exist in the heap and is out of bounds. 
    # Therefore, the condition self.arr[l] > self.arr[i] should not be checked as it may cause an index out of range error.

    # after the first 2 if statements, the 3rd if statement checks if i, the parent node is still the largest.
    # if i != largest, then it means one of child nodes are now the stored in the largest variable.
    # b/c to maintain maxHeap property, and child is larger than parent node, need to swap the parent node and the child node.
    # 1) store parent node into temp node variable => 2) store child node(largest) in the parent node variable (self.arr[i])
    # 3) the original parent which was stored in the temp variable will now be transferred into the original child variable(self.arr[largest])
    # 4) invoke maxHeapify now on the child node which used to be the original parent node in that sub-tree, before being swapped. 
    def MaxHeapify(self, i):
        l = self.lChild(i)
        r = self.rChild(i)
        largest = i
        if l < self.heapSize and self.arr[l] > self.arr[i]:
            largest = l
        if r < self.heapSize and self.arr[r] > self.arr[largest]:
            largest = r 
        if largest != i:
            temp = self.arr[i]
            self.arr[i] = self.arr[largest]
            self.arr[largest] = temp
            self.MaxHeapify(largest)
 
    # Returns the index of the parent of the element at ith index.
    def parent(self, i):
        return (i - 1) // 2
 
    # Returns the index of the left child.
    def lChild(self, i):
        return (2 * i + 1)
 
    # Returns the index of the right child.
    def rChild(self, i):
        return (2 * i + 2)
 
    # Removes the root which in this case contains the maximum element.
    def removeMax(self):
        # Checking whether the heap array is empty or not.

        # if only 1 element, then reduce the size, then return the max at self.arr[0]
        if self.heapSize <= 0:
            return None
        if self.heapSize == 1:
            self.heapSize -= 1
            return self.arr[0]
 
        # Storing the maximum element to remove it.

        # storing the root in root variable => replacing the root with the last element in the heap (self.heapSize -1)
        # then reduce the size of heap by 1.
        root = self.arr[0]
        self.arr[0] = self.arr[self.heapSize - 1]
        self.heapSize -= 1
 
        # Then, need to restore the property of the Max heap.
        # after removing, the maxheap is out of order.
        self.MaxHeapify(0)
 
        # return the root which will contain the max element.
        return root
 
    # Increases value of key at index 'i' to new_val.

    # after changing value at index i, => while i is not the root and i's value greater than it's parent's => store value of i in temp
    # then set the parent's value into i's former variable/shell (self.arr[i])
    # then set i's new value(stored in temp value) as the parent of (i), and i is now the former parent as is smaller than child (former i).
    # then set the i variable as the parent of i.
    # pretty much like maxHeapify again.
    # its in a while loop, so it keeps on going until the while loop condition breaks.

    def increaseKey(self, i, newVal):
        self.arr[i] = newVal
        while i != 0 and self.arr[self.parent(i)] < self.arr[i]:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = temp
            i = self.parent(i)
 
    # Returns the maximum key
    # (key at root) from max heap.
    def getMax(self):
        return self.arr[0]
 
    def curSize(self):
        return self.heapSize
 
    # Deletes a key at given index i.
    def deleteKey(self, i):
        # It increases the value of the key
        # to infinity and then removes
        # the maximum value.
        self.increaseKey(i, float("inf"))
        self.removeMax()
 
    # Inserts a new key 'x' in the Max Heap.
    def insertKey(self, x):
        # To check whether the key
        # can be inserted or not.
        if self.heapSize == self.maxSize:
            print("\nOverflow: Could not insertKey\n")
            return
 
        # The new key is initially
        # inserted at the end.
        self.heapSize += 1
        i = self.heapSize - 1
        self.arr[i] = x
 
        # The max heap property is checked
        # and if violation occurs,
        # it is restored.
        while i != 0 and self.arr[self.parent(i)] < self.arr[i]:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = temp
            i = self.parent(i)
 
 
# Driver program to test above functions.
if __name__ == '__main__':
    # Assuming the maximum size of the heap to be 15.
    h = MaxHeap(15)
 
    # Asking the user to input the keys:
    k, i, n = 6, 0, 6
    print("Entered 6 keys:- 3, 10, 12, 8, 2, 14 \n")
    h.insertKey(3)
    h.insertKey(10)
    h.insertKey(12)
    h.insertKey(8)
    h.insertKey(2)
    h.insertKey(14)
 
    # Printing the current size
    # of the heap.
    print("The current size of the heap is "
          + str(h.curSize()) + "\n")
 
    # Printing the root element which is
    # actually the maximum element.
    print("The current maximum element is " + str(h.getMax())
          + "\n")
 
    # Deleting key at index 2.
    h.deleteKey(2)
 
    # Printing the size of the heap
    # after deletion.
    print("The current size of the heap is "
          + str(h.curSize()) + "\n")
 
    # Inserting 2 new keys into the heap.
    h.insertKey(15)
    h.insertKey(5)
    print("The current size of the heap is " + str(h.curSize()))