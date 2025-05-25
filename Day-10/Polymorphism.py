# Method overloading not allowed
class Demo:
    def Addition(self,A,B):
        return A+B
    
    def Addition(self,A,B,C):
        return A+B+C
    
obj = Demo()

print(obj.Addition(10,11))
print(obj.Addition(10,11,21))