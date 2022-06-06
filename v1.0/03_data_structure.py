#-*- coding: euc-kr -*-#

# ����Ʈ (list)
# ����: [], list()
# ������ ��ü�� ���������� �����ϴ� �ڷ���

L = [1, 2, 3]
L = list([1, 2, 3])
print(L)
print(type(L))

print(L[0]) # indexing
print(L[0:2]) # slicing
print(L[0:3:2]) # slicing
print(len(L)) # length: 3
print(L + L)
print(L * 3)
print(1 in L) # membership test

L[0] = 10
print(L)

#################
s = "hello world"
#s[0] = 'H' # ?? # �Ұ���, ���ڿ��� ����̱� ����
s = 'H' + s[1:]
#################

# Ʃ�� (tuple)
# ����Ʈ�� ����
# Ʃ�� ���� ���Ҹ� ������ �� ���� (immutable)
# ex) 1 ~ 12��, 1 ~ 31��
# ����: (), tuple()
t = ('January','February','March','April','May','June','July','August','September','October','November','  December')
#t[0] = 'Jan' # �Ұ���, Ʃ���� ����̱� ����

print(t[0])
print(t[-1])
print(t[0:2])
print(t[0:5:2])
print(t + t + t)
print(t * 2)
print('July' in t) # membership test (in, not in)

# ���� (dictionary; dict)
# Ű (key)�� ���� �� (value)�� �����ϴ� �ڷ� ����
# Map �ڷ� ������ ����
# ����: {}, dict()

d = {'a':'apple','b':'banana'}
print(d['a'])

d['a'] = 'ant' # ���� ���� ���� (mutable)

# ���� �߰�
d['k'] = 'kiwi'

# membership test (Ű ���� ����)
print('a' in d)

# Ű ����
print(d.keys())

# �� ����
print(d.values())

# (Ű, ��) Ʃ�� ���� ����
print(d.items())