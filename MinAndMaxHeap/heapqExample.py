import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        # Push the negative of the item to simulate a max-heap
        heapq.heappush(self.heap, -item)

    def pop(self):
        # Pop the negative of the item to get the original value
        return -heapq.heappop(self.heap)

    def peek(self):
        # Peek at the top item without popping it
        return -self.heap[0]

    def __len__(self):
        return len(self.heap)

# Example usage
if __name__ == "__main__":
    max_heap = MaxHeap()
    max_heap.push(10)
    max_heap.push(20)
    max_heap.push(15)

print("Max value:", max_heap.peek())  # Output: Max value: 20

print("Popped value:", max_heap.pop())  # Output: Popped value: 20
print("Max value after pop:", max_heap.peek())  # Output: Max value after pop: 15
