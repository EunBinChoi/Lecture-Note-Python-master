#-*- coding: euc-kr -*-#

# ���� (lambda) �Լ� (��� �Լ�)
# : �Ϲ����� �Լ��� �� �ٷ� ������ �� ����
# : �Լ� �̸��� ���� ��ȸ������ ����� �Լ��� ���ؼ� ��� 
# (�͸� �Լ�)

def incr(x):
    return x + 1

print(incr(1))
print(incr(2))

# lambda function (python)
f = lambda x: x + 1
print(f(1))

# lambda (java)
# (parameter) -> {return}

f = lambda x, y=1: x + y # y default: 1
print(f(1, 2))
print(f(10))

# ���� ���ڸ� ������ ���� �Լ�
vargs = lambda *args: args
print(vargs())
print(vargs(1))
print(vargs(1, 2, 3))

func_list = [
    lambda x, y : x + y,
    lambda x, y : x - y,
    lambda x, y : x * y,
    lambda x, y : x / y
]

print(func_list[0](3, 5)) # +
print(func_list[1](3, 5)) # -
print(func_list[2](3, 5)) # *
print(func_list[3](3, 5)) # /

############################################
# lambda + map()

# map(function, sequence �ڷ��� (list, tuple, string))

def f(x):
    return x * x

l = list(range(1, 6)) # 1 ~ 5
m = list(map(f, l))
print(m)

m = list(map(lambda x: x * x, l))
print(m)

# Q1.
# range(10)�� ��� �� x�� ���� 
# f = x * x + 4 * x + 5�� ��� ��� ����Ʈ�� ��ȯ

f = lambda x: x * x + 4 * x + 5
m = list(map(f, list(range(10))))
print(m)

# Q2.
# ["hello", "python", "java"] �� �ܾ���� ���� ����Ʈ�� ��ȯ
l = ["hello", "python", "java"]
L = [len(i) for i in l] # list comprehension

f = lambda x: len(x)
m = list(map(f, l)) # map
print(m)


# filter(function, sequence �ڷ��� (list, tuple, string))
f = lambda x: x > 2
fi = list(filter(f, range(10)))
print(fi)

# Q1. range(10) �߿��� ¦���� ���͸�
f = lambda x: x % 2 == 0
fi = list(filter(f, range(10)))
print(fi)


# Q2. l = ["hello", "python", "java"] �߿��� 
# ���ڿ��� ���̰� 5 �ʰ��� �ܾ� ���͸�
l = ["hello", "python", "java"]
f = lambda x: len(x) > 5
fi = list(filter(f, l))
print(fi)

# Q3. s = 'abc123'���� ���ĺ��� ���͸�
s = 'abc123'
#f = lambda x: 'a' <= x.lower() <= 'z'
f = lambda x: x.isalpha() 
fi = list(filter(f, s))
print(fi)

# reduce(function, sequence �ڷ��� (list, tuple, string))
# python3 -> ���� �Լ� �ƴ�

from functools import reduce
f = lambda x, y: x + y
re = reduce(f, range(5)) # 0 ~ 4 (0 + 1 + 2 + 3 + 4)
print(re)

"""
x y reduce
0 0 0
0 1 1
1 2 3
3 3 6
6 4 10
"""

f = lambda x, y: x + y
re = reduce(f, range(5), 100) # 0 ~ 4 (0 + 1 + 2 + 3 + 4)
print(re)

"""
x   y  reduce
------------
100 0  100
100 1  101
101 2  103
103 3  106
106 4  110
"""


re = reduce(lambda x, y: y + x, 'abc', "") 
print(re)

"""
x   y  reduce
------------
"" a     a
a  b    ba
ba c   cba
"""
