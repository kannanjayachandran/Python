from collections import deque

queue = deque()

queue.append(25)
queue.append(50)

print(queue)

queue.popleft()
print(queue)

queue.appendleft(75)
print(queue)
