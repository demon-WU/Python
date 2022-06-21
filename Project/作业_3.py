import types
@classmethod
def catMethod(cls):
    print('OK')
    pass
def run(self):
    print('跑起来')
    pass
pass
class Animal:
    pass
Animal.anMethod=catMethod
cat=Animal()
cat.anMethod()
cat.colour='蓝色'
cat.inputRun=types.MethodType(run,cat)
cat.inputRun()
print(cat.colour)