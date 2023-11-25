class Coorutine_1:
    def __init__(self, name) -> 'Coorutine_1': # тут self
        self.name = name
        
    def __str__(self) -> str:
        return f'{self.name}'
    
class Coorutine_2:
    def __init__(cls, name) -> 'Coorutine_2': # тут cls
        cls.name = name
        
    def __str__(cls) -> str:
        return f'{cls.name}'
    
    
c1 = Coorutine_1('Hello')
c2 = Coorutine_2('Hello')

print(c1, c2) # Hello Hello