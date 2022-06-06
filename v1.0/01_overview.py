#-*- coding: euc-kr -*-#

# single line comment
"""
multiple line comment
multiple line comment
multiple line comment
"""

# ���̽� (Python)
# ��ũ��Ʈ (Script) ���
# ������ ���� �޸� �ҽ��ڵ带 ���� ���� �о �ٷ� ���� (����������)
# ����: ���� �ð� ����, �ҽ� �ڵ� ������ ����
# ����: ���� �ӵ� ���� �ɸ�

# ex) JavaScript, Python, Ruby 

print("hello world")
print('hello world')

# ������ ������ Ÿ�� ���� 
a = 10 # data type�� ����
print(a)
print(type(a))

a = "string"
print(a)
print(type(a))

def add(a, b):
    return a + b

print(add(3, 5))
print(add("abc", "def"))

# ������ (+, -, *, /, **)
print(3 / 5) # ���� / ���� = �Ǽ�
print(3 ** 3) # 3�� 3��

# ����ڿ��� ������ �Է� (input() => ������ string���� ����!)
name = input('name ? ') 
print(name)
print(type(name)) # class 'str'

age = int(input('age ? '))
print(age)
print(type(age)) # class 'int'


# ���� ����
test = 10

# ���� ����
del test
#print(test) # ��� �Ұ�

# �� ���� swap �ڵ�
x = 10
y = 20
tmp = x
x = y
y = tmp

x, y = y, x # ���� ġȯ ����

# ���� �Լ� (built-in function)
# ���� ��� �߰� ���� �⺻ ���� �Լ�

# ���밪 ��ȯ
print(abs(3))
print(abs(-3))

print(max(3, 5))
print(min(3, 5))

print(3 ** 3)
print(pow(3, 3))
