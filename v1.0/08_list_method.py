#-*- coding: euc-kr -*-#

# �ϳ��� ���� �߰�
s = [1, 2, 3]
s.append(4) # ����Ʈ �� �������� ���� 4 �߰�
s.insert(3, 10) # �ε��� 3 ��ġ�� ���� 10 �߰�
print(s)

# [1, 2, 3, 10, 4]
#  0  1  2  3   4

print(s.index(3)) # �� 3�� �ε��� ��ȯ

s = [10, 10, 10, 10]
print(s.count(10)) # �� 10�� ���� ��ȯ

# sort() vs sorted()
s = [1, 2, -10, -7, 100]
ss = s.sort()
print(s) # sort() �Լ��� s ��ü�� ���ĵ�
print(ss) # sort() �Լ��� ��ȯ���� ����

s = [1, 2, -10, -7, 100]
ss = sorted(s)
print(s) # sorted() �Լ��� s �״�� ���ΰ�
print(ss) # ���ĵ� s�� ��ȯ

# reverse() vs reversed()
s = [1, 2, -10, -7, 100]
sr = s.reverse()
print(s) # reverse() �Լ��� s ��ü�� ������
print(sr) # reverse() �Լ��� ��ȯ���� ����

s = [1, 2, -10, -7, 100]
sr = reversed(s)
print(s) # reversed() �Լ��� s �״�� ���ΰ�
print(list(sr)) # ������ s�� ��ȯ

# ���� ����
# remove() & del & pop()
s = [10, 20, 30, 40, 50]
s.remove(10) # ���� ... ���Ұ��� �˻��ϴ� �ð��� �ɸ�
print(s)

del s[2]
print(s)

s.pop() # �ε����� ������ ������ ���� ���� (stack pop())
s.pop(1)
print(s)
print()

print()
print()
print()

# [] ������ ���� �߰�
# append() vs extend()
s = [10, 20, 30, 40, 50]
s.append([60, 70])
print(s)
print(len(s)) # 6
print(s[5]) # [60, 70]
print(s[5][1]) # 70 
print()

s = [10, 20, 30, 40, 50]
s.extend([60, 70])
print(s)
print(len(s)) # 7
print(s[5:7]) # [60, 70]
print(s[6]) # 70

ls = [10, 20, 30, 40, 50]
rs = [60, 70]
s = ls + rs
print(s)

# �ϳ��� ���� �߰��� �� (append, insert)
s = [10, 20, 30, 40, 50]
s.append(60)
#print(s)


# list -> stack(LIFO), queue(FIFO)
# stack
s = [10, 20, 30, 40, 50]
print(s.pop())
s.append(60)
print(s)

# queue
s = [10, 20, 30, 40, 50]
print(s.pop(0))
s.append(60)
print(s)


#################################################
# list comprehension (����Ʈ ����) + for��


# ���п��� ���� ǥ���
# A = {x^2 | x in {0,...,9}} = {0, 1, 4, 9, 16, ...., 81}


# �Ϲ� for���� �̿��ؼ� ����Ʈ ����
L = []
for i in range(10): # 0 ~ 9
    L.append(i**2)
print(L)

# list comprehension
L = [i**2 for i in range(10)]
print(L)


###################################################

# �Ϲ� for���� �̿��ؼ� ����Ʈ ����
L = []
for i in range(10): # 0 ~ 9
    if i % 3 == 0:
        L.append(i**2)
print(L)

# list comprehension
L = [i**2 for i in range(10) if i % 3 == 0]
print(L)


###################################################

# list comprehension
seq1 = 'abc'
seq2 = (1, 2, 3)
# [(a, 1), (a, 2), (a, 3), (b, 1), (b, 2), (b, 3), ...]
L = [(i,j) for i in seq1 for j in seq2]
print(L)

# Q1.
# �Ϲ� for���� �̿��ؼ� ����Ʈ ����
L = []
seq1 = 'abc'
seq2 = (1, 2, 3)

for i in seq1:
    for j in seq2:
        L.append((i, j))

print(L)

###################################################

# Q2.
# ������ + ����Ʈ ������
# L = [(2,1,2), (2,2,4), (2,3,6), (2,4,8),....]

L = [(x, y, x*y) for x in range(2, 10) for y in range(1, 10)]
print(L)

# Q3.
s = 'spam and egg'
li = s.split('and')
print(li) # 'spam ', ' egg'

li_strip = [i.strip() for i in li]
print(li_strip)

li_strip = [i.strip() for i in s.split('and')]
print(li_strip)

# Q4.
s = 'The quick brown fox jumps over the lazy dog'
# [(The, 3), (quick, 5), (brown, 5) ,...] 

L = [(voca, len(voca)) for voca in s.split()] # ['The', 'quick', ...]
print(L)

# Q5.
# ��Ÿ��� (x*x + y*y = z*z)�� �����ϴ� �ﰢ�� ������ (x,y,z) ��
# 1 <= x, y, z < 100
# (3, 4, 5), (5, 12, 13), (6, 8, 10) 

L = [(x,y,z) for x in range(1, 100) 
for y in range(1, 100) 
for z in range(1, 100) 
if x*x + y*y == z*z and x <= y <= z and x + y > z]


print(L)
print(len(L))

