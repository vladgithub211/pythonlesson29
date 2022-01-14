class Car:
    def __init__(self,marka,model,year):
        self.marka = marka
        self.model = model
        self.year = year
        self.adomiter = 0
    def update_adomiter(self,n):
      if n>=self.adomiter:
        self.adomiter = n
      else:
        print(f"Пробег скинуть невозможно")
    def ink_adomiter(self,m):
        self.adomiter+=m
        print(f"Ваша машина проехала:{self.adomiter}")
    def read_adomiter(self):
        print(f"Марка:{self.marka},Модель:{self.model},Год выпуска:{self.year},Пробег машины:{self.adomiter}")
    def get_descript_name(self):
        print(f"Марка:{self.marka},Модель:{self.model},Год выпуска:{self.year}")
class Electro(Car):
    def __init__(self,marka,model,year,battary):
        Car.__init__(self,marka,model,year)
        self.battary = battary
    def bat(self,b):
        print(f"Марка:{self.marka},Модель:{self.model},Год выпуска:{self.year},Пробег машины:{self.adomiter},Батарея:{self.battary}")
    def user(self,a):
      if a>=1000000:
          print("Машина ваша")
      else:
          print("Машина не ваша")
c1 = Car("Tesla","Cybertrack",2022)
n = int(input("Введите начальный пробег="))
m = int(input("Введите второй пробег="))
b = int(input("Введите кол-во батареи="))
a = int(input("Введите стоимость машины"))
#c1.adomiter=23
c1.get_descript_name()
c1.update_adomiter(n)
c1.read_adomiter()
c1.ink_adomiter(m)
c1.bat(b)
c1.user(a)

