from collections import Counter

p = 'hello there how are you !'

count = Counter(p)
print(count)
# Counter({' ': 5, 'e': 4, 'h': 3, 'o': 3, 'l': 2, 'r': 2, 't': 1, 'w': 1, 'a': 1, 'y': 1, 'u': 1, '!': 1})


# if you want a specific charater count then
print(count[' '])
# 5


print (list(count.elements()))
# ['h', 'h', 'h', 'e', 'e', 'e', 'e', 'l', 'l', 'o', 'o', 'o', ' ', ' ', ' ', ' ', ' ', 't', 'r', 'r', 'w', 'a', 'y', 'u', '!']


# to find the most common word
print( count.most_common(2))
# [(' ', 5), ('e', 4)]


seconed_count = Counter('hey ! how are you')
print(count.subtract(seconed_count))
# None

# but now if you try to print count then it shows you the subtracted count
print(count)
# Counter({'e': 2, 'l': 2, 'h': 1, 'o': 1, ' ': 1, 't': 1, 'r': 1, 'w': 0, 'a': 0, 'u': 0, '!': 0, 'y': -1})