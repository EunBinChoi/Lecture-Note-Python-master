# lambda function (람다 함수, 축약 함수)
# : 일반 함수 정의 (def) 없이 한 줄로 정의할 수 있음
# : 함수의 이름이 없이 일회성으로 사용할 함수 (익명 함수)

def add(a, b=1):
    return a + b

res = add(1) # 2
res = add(1, 2) # 3

from collections.abc import Iterable

def vars(*args):
    print(args)
    print(type(args)) # tuple
    for ele in args:
        if isinstance(ele, Iterable):
            for e in ele:
                if isinstance(e, Iterable):
                    vars(e)
                else:
                    print(e)
        else:
            print(ele)     

vars()
vars(1)
vars(1, 2, 3, 4, 5, 6)
print("asdasdasd ", end='')
vars(range(10)) # ([0, 1, 2, 3, 4, ... 9], ) 

def varss(**args):
    print(args)
    print(type(args)) # dict
    for key, value in args.items():
        print(key, value)

varss(first='1', mid='2', last='3')
varss(a='1', b='2', c='3')
varss(a='1', b='2', c='3', d='4')
varss(A='1', B='2', C='3', D='4')
varss()

def varsss(a, *args):
    print(a) # 1
    print(args) # (2, 3, 4, 5)
varsss(1, 2, 3, 4, 5)


a, *args = (1, 2, 3, 4, 5)
print(a)
print(args) # type: list

numbers = [1, 2, 3, 4, 5]
li = [*numbers, 10, 20]
li = [numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], 10, 20]
print(li)

#############################################################
def f(a, b=1):
    return a + b

f = lambda a, b=1: a + b
f = lambda *args: args

f()
f(1)
f(1, 2, 3, 4)

func_list = [
    lambda x, y: x + y,
    lambda x, y: x - y,
    lambda x, y: x * y,
    lambda x, y: x / y
]

for func in func_list:
    print(func(1, 2))

#############################################################
# lambda + map(func, seq), filter(func, seq), reduce(func, seq)

# map
res = list(map(lambda x : x*x, [1, 2, 3]))
print(res)

# list comprehension
li = [1, 2, 3]
res = [ele**2 for ele in li]
print(res)

# filter
res = list(filter(lambda x : x % 2 == 0, range(10)))
print(res)

s = 'abc123' 
res = list(filter(lambda c : c.isalpha(), s))
res = "".join(res)
print(res)

# reduce
from functools import reduce
res = reduce(lambda x, y : x + y, range(5), 100)
print(res)

# x의 초기값을 지정하지 않으면 y의 첫번째 값을 x의 초기값으로 지정
# y의 첫번째 값 ==> 1
res = reduce(lambda x, y : x * y, range(1, 6))
print(res)

"""
x  y (range(5)) = 0 ~ 4
----
0  0
0  1
1  2
3  3
6  4
10
"""

res = reduce(lambda x, y : y + x, ['a', 'b', 'c'])
print(res)