import sys
import inspect
# from ..sub2 import module2

# module1.py
def mod2_test1():
    print("Module1 -> Test1")
    print("Path : ", inspect.getfile(inspect.currentframe()))

def mod2_test2():
    print("Module1 -> Test2")
    print("Path : ", inspect.getfile(inspect.currentframe()))