# dict: sequence datatype X
# (key, value) == item (java Entry<K, V>)

d = {'a':1, 'b':2, 'c':3}
d['a'] = 10
print(d)

#print(d['d']) # error

d['d'] = 4 # 원소 추가
print(d)

# zip() (***)
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = dict(zip(keys, values))
print(d)

d = list(zip(keys, values))
print(d)

d = {'a':10, 'b':2, 'c':30}
for key, value in d.items():
    print(key, value)

items = list(d.items()) # [('a', 10), ('b', 2), ('c', 30)]
items.sort(key=lambda x : x[0], reverse=True)
print(items)