class Home:
    def __init__(self, name, area):
        self.name = name
        self.area = area
        self.all = area
        
    def bring(self):
        print(f"house tepy: {self.name}")
        print(f"размер дома: {self.area} м**2")
        self.__bed()
        self.__Wardrode()
        self.__table()
        print("заносим мебель")
        print(f"осташее место: {self.area}")
        
        
    def __bed(self):
        self.area -= 4
        
    def __Wardrode(self):
        self.area -= 2
        
    def __table(self):
        self.area -= 1.5
        
mda = Home("элитка", 100)
mda.bring()
    