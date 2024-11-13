#temperature converted: celcius to ferhenheit,ferhenheit to celcius
#ask user fer temperature value and also for unit

class temperature:
  def __init__(self,temp,unit):
    self.temp=temp
    self.unit=unit

  def celsius_to_feh(self):
    if self.unit=="celsius":
      print((self.temp*9/5)+32)
    else:
      print((self.temp-32)*5/9)

temp= float(input("Enter temperature value"))
unit= input("Enter unit ")

obj=temperature(temp,unit)
obj.celsius_to_feh()
