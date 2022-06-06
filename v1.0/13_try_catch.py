#-*- coding: euc-kr -*-#

# ���� ó�� (exception handling)
# try/except/else/finally


"""
try:
    ���� �߻� ������ ����
except Exception:
    ���� �߻��� ������ ����
else:
    ���� �߻����� �ʾ��� �� ������ ����
finally:
    ���� �߻� ���� ������� ������ ������ ����

"""

try:
    print(1 / 0)
except ZeroDivisionError as e:
    print(e)

try:
    a()
except NameError as e:
    print(e)

try:
    a = 1
    print(1 / 0) # ZeroDivisionError
    b() # NameError
    print('2' + 2) # str + int (x) # TypeError
except ZeroDivisionError as e:
    print(e)
except NameError as e:
    print(e)
except TypeError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print('success!')
finally:
    print('finally')


# IOError (���� ����ó��)
try:
    with open('test.txt', 'r') as f:
        s = f.read()
        print(s)
except IOError as e:
    print(e)


# ���� �߻�
a = 10
b = 0
try:
    if(b == 0):
        raise ArithmeticError('0���� ������ �ֽ��ϴ�!')
    a / b
except ArithmeticError as e:
    print(e)