class A():
    def run(self):
        print("A")

class B():
    def run(self):
        print("B")    

class C(A, B):
    pass

aobj = A()
aobj.run()

bobj = B()
bobj.run()

cobj = C()
print(C.mro())
cobj.run()