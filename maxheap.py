import heapq

listfortree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

minheap = heapq.heapify(listfortree)
maxheap = heapq._heapify_max(listfortree)

print heapq.heappop(listfortree)
print heapq._heappop_max(listfortree)

print minheap, maxheap
