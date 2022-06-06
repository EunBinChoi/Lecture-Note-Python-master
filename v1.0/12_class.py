#-*- coding: euc-kr -*-#

# ���̽� Ŭ����

class S1:
    pass # ����, �Լ� ���ǰ� ���� (body�� ����ִ� Ŭ����)


class S: # header
    a = 1 # body

    # constructor (������)
    def __init__(self, a=None):
        if a:
            self.a = a
            print("constructor")
        else:
            print("constructor")

    # destructor (�Ҹ���)
    def __del__(self):
        print("destructor")

    # toString()
    def __str__(self):
        return "a : " + str(self.a) # str + str(int)  

    # getter, setter
    def setA(self, a): # self: �ν��Ͻ� �ڽ��� ���۷����� ������ ����
        print(self)
        self.a = a
    
    def getA(self):
        print(self)
        return self.a

    # instance�� ȣ���ϴ� �� �ƴϰ� Ŭ�����̸�.method(1, 2)
    @staticmethod # decorator (�����)
    def method(x, y):
        print('static method : ', x, y)



# Ŭ�����̸�.�����̸� ���� ���� 
print(S.a) # static variable
S.a = 2
print(S.a)

# ��ü�� ���� ��ü�̸�.�����̸����� ����
instance1 = S()
print(instance1.a) # instance variable
instance1.a = 3
print(instance1.a) # 3
print(S.a) # 2


# ��ü�� ���� ��ü�̸�.�����̸����� ����
instance2 = S()
print(instance2.a) # instance variable
instance2.a = 10
print(instance2.a) # 10
print(instance1.a) # 3
print(S.a) # 2

instance3 = S()
# setter
instance3.setA(10) # self => instance3
# getter
res = instance3.getA() # self => instance3
print(res)

# ���� �ڵ�� �Ʒ��� ����
S.setA(instance3, 10)
res = S.getA(instance3)
print(res)

instance4 = S(20)
print(instance4)

###################################################

# class inheritance (���)

class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def __str__(self):
        return "<Person {0} {1}>".format(self.name, self.phone)

class Employee(Person): # extends Person (java)
    def __init__(self, name, phone, position, salary):
        super().__init__(name, phone)
        self.position = position
        self.salary = salary

    def __str__(self):
        # \ : �ڵ��� ���̰� ����� �� �ڵ��� ������ ���� ���
        return super().__str__().replace("Person", "Employee")[:-1] \
        + " {0} {1}>".format(self.position, self.salary)

# <Person eunbin 1234> -> <Employee eunbin 1234 lecturer 3000>

p = Person("eunbin", "1234")
e = Employee("eunbin", "1234", "lecturer", "3000")
print(p)
print(e)

###################################################
# ������ (polymorphism)
# ��� ���� ������ �ٸ� Ŭ�������� �ν��Ͻ����� 
# ���� ��� �Լ��� ȣ���ص�
# ���� �ٸ��� �����ϴ� ���
# ex) �Լ��� �����ε��� ������ �߿� �ϳ�
def add(a, b): # str (���ڿ� ����), int (��ġ ����)
    return a + b 

# parent -> {child, child, child ...}

class Animal:
    def cry(self):
        print('....')

class Dog(Animal):
    def cry(self):
        print('�۸�!')

class Cat(Animal):
    def cry(self):
        print('�߿�~')

ani = [Dog(), Cat()] # Dog, Cat ��ü�� ����Ʈ�� ���������� ����

for i in ani:
    i.cry()


