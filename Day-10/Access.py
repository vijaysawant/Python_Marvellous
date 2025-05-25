# Access specifiers in Python. Public, Protected and Private

class Student:
    def __init__(self,A,B,C):
        self.Name = A       # Public instance variable
        self._Age = B       # Protected instance variable
        self.__marks = C    # Private instance variable

    def Display(self):
        print(self.Name)
        print(self._Age)
        print(self.__marks)

obj = Student("Rahul", 24, 89)
obj.Display()

print(obj.Name)
print(obj._Age)
# print(obj.__marks)
