
# The defaultdict is a subclass of Python’s dict that accepts a default_factory as its primary argument.
# The default_factory is usually a Python type, such as int or list, but you can also use a function or a lambda too.






from collections import defaultdict

sentence = "The world is filled with nice people if you can't find one Be one"
words = sentence.split(' ')
d = defaultdict(int)

for each in words:
    d[each] += 1

print(d)
# defaultdict(<class 'int'>, {'The': 1, 'world': 1, 'is': 1, 'filled': 1, 'with': 1, 'nice': 1, 'people': 1, 
#                                  'if': 1, 'you': 1, "can't": 1, 'find': 1, 'one': 2, 'Be': 1})
