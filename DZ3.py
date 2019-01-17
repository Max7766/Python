class Human:
    def __init__(self,name=None,age=None):
        self.name=name
        self.age=age
    def name_age(self):
        if type(self) is str or int:
           print(self.name,self.age)
    def say_hello(self_name=' Max'):
        if type(self_name)is str:
            return 'Hello,my name is{}'.format(self_name)
var=Human(name='Max',age='23')
print(var.name_age())
print(Human.say_hello())

class builder(Human):
    def __init__(self,doljnost=' brigadir'):
       self.doljnost=doljnost
       super().__init__()
    def dol(self):
        return 'Должность is:{doljnost}'.format(doljnost=self.doljnost) 

bar=builder()
print(bar.dol())
print(bar.say_hello())
class Write(Human):
    def my_books(*args):
        d=0
        for x in args :
            if str(type(x))not in args :
                d+=1
                return 'I write-{}'.format(d)



als=Write.my_books('Harry Potter',False,'Metro','Stalker',2,5)
print(als)

        
        
        






    
     
        
        
        
        
  



