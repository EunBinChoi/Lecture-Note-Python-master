#-*- coding: euc-kr -*-#

# ��� (module)
# �Լ�, ����, Ŭ������ ������� ����
# 1) ǥ�� ��� (���̽� ��� ��Ű������ �⺻ ����)
# ex) import os, import shutil .....
# 2) ����� ���� ��� (�����ڰ� ���� ������ ���)

# �̸� ���� (namespace, scope)
# ���� ������ �����ϴ� ��� (���� (local), ���� (global))

g = 10 # global
h = 5 # global

def f(a): # a: local
    h = a + 10 # h: local
    print(g) # global
    print(h) # global, local (�켱����: local > global)

f(1)
print(h) # global # 5

#######################################
print() # enter
print() # enter

g = 10 # global
h = 5 # global

def f(a): # a: local
    global h # global ������ h�� �Լ� ������ ����ϰڴ�!
    h = a + 10 # h: global
    print(g) # global
    print(h) # global

f(1)
print(h) # global # 11

#####################################

g = 10

def f():
    global g
    a = g # g: global
    g = 20

f()
print(g)

#################################

import mymath # ����� ���� ���

print(mymath.mypi)
print(mymath.area(5))


########################################
# ��� import ���

# import ���� [as mm] # ��� ��Ī
import mymath as mm
print(mm.mypi) # ��� �̸� �ۼ� �ʿ�
print(mm.area(5)) # ��� �̸� �ۼ� �ʿ�

# from ���� import �̸� 
from mymath import *
print(mypi) # ��� �̸� ���� ���� ��� ����
print(area(5)) # ��� �̸� ���� ���� ��� ����