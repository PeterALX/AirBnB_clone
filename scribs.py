#!/usr/bin/python3

d = {'a': [1, 2, 3], 'b': {1, 2, 3}}

b = d['a']
print(d)
del d['a']

print(d)
print(b)
