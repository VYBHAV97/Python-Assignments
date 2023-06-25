# Python program to demonstrate queue implementation using list

# Initializing a queue
queue = []

# Adding elements to the queue
queue.append('1st Element')
queue.append('2nd Element')
queue.append('3rd Element')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")

#Pop the elements untill queue is empty
while queue:
    print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)
