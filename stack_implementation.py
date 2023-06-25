# Python program to demonstrate stack implementation using list

stack = []

# append() function to push element in the stack
stack.append('1st Element')
stack.append('2nd Element')
stack.append('3rd Element')

print('Initial stack')
print(stack)

# pop() function to pop element from stack 
print('\nElements popped from stack:')

#Pop the elements untill stack is empty
while stack:
    print(stack.pop())

print('\nStack after elements are popped:')
print(stack)
