# tuple: sequence datatype
# indexing, slicing, +, *, membership test, len(), for ~ in
# packing, unpacking
# ()

# tuple: immutable (******)

tu = 1, 2, 3
print(tu)
print(type(tu))

li = list(tu)
li[0] = 10

# set (집합) (원소 중복 불가)
# set([1, 2, 3]) == set([3, 2, 1])
# 원소 간의 순서가 존재하지 않음 (indexing X, slicing X ....)
s = set([1, 2, 3, 4, 3, 3, 3])
print(s)
print(len(s))
print(1 in s)

for el in s:
    print(el)

#for idx in range(len(s)): # error
#    print(s[idx])

#s[0] = 10
#print(s)

dic = {'a':1, 'b':2, 'c':3} # dict
print(dic)
print(type(dic))

s = {1, 2, 2, 3} # set (dict key처럼 hash table에 저장)
print(s)
print(type(s))
print()

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
union = s1.union(s2) # 합집합
union = s1 | s2
print(union)

inter = s1.intersection(s2) # 교집합
inter = s1 & s2
print(inter)

differ = s1.difference(s2) # 차집합
differ = s1 - s2
print(differ)

s1 = {4, 5, 6, 10, 20, 30}
s2 = {10, 20, 30}
print(s2.issubset(s1))
print(s1.issuperset(s2))