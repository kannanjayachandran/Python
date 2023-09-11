import heapq

minHeap = []
heapq.heappush(minHeap, 10)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 5)
heapq.heappush(minHeap, 3)

# min element will always be at the 0-th index
while len(minHeap):
    print(heapq.heappop(minHeap))
