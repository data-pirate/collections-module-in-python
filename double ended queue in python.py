from collections import deque
import string

x = list(string.ascii_lowercase)
d = deque(x)
# deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
#       'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
for letter in d:
    print(letter)

d.append('hello')
d.append('bye')

print(d)
# deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
#        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'hello', 'bye'])

d.rotate(2)
print(d)
# deque(['hello', 'bye', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
#         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
