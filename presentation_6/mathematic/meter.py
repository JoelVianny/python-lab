class Distance:
    def __init__(self, feet=0, inches=0):
        total_inches = feet * 12 + inches
        self._feet = total_inches // 12  
        self._inches = total_inches % 12

    def add__(self, other):
        
        total = self.total_inches() + other.total_inches()
        return Distance(0, total)
    
    def sub__(self, other):

        total = self.total_inches() - other.total_inches()
        return Distance(0, total)
    
    def total_inches(self):
        
        return self._feet * 12 + self._inches
    
    def str__(self):

        return f"{self._feet} feet {self._inches} inches"


d1 = Distance(3, 14)  
d2 = Distance(2, 8)   

d3 = d1 + d2
print(d3)  

d4 = d1 - d2
print(d4)  

