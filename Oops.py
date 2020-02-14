class vehicle:
  def __init__(self,name,type,color):
    self.name=name
    self.type=type
    self.color=color

a=vehicle("Honda","car","red")
b=vehicle("Yamaha","bike","blue")
print(a.name,"\n",b.type)
c= isinstance(a,vehicle)
print(c)

class four_wheeler(vehicle):
  def __init__(self,CC,Gears):
    self.CC=CC
    self.Gears=Gears

f=four_wheeler(1800,6)
print(f.CC)
k=issubclass(four_wheeler,vehicle)
print(k)