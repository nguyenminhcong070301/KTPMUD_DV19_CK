n = float(input("Moi nhap real_number: "))
m = float(input("Moi nhap image_number: "))
class Sothuc :
    def __init__(self,real_number) :
        self.real_number = real_number
    def gttd(self) :
        return (self.real_number **2) ** 0.5 
    
class Sophuc(Sothuc) :
    def __init__(self,real_number, image_number) :
        super().__init__(real_number)
        self.image_number = image_number
    def module(self) :
        return (self.image_number**2 + self.real_number**2) ** 0.5
  
sothuc = Sothuc(n)
print("Tri tuyet doi co gia tri la: ",sothuc.gttd())

sophuc = Sophuc(n,m)
print("module cua so phuc la: ",sophuc.module())