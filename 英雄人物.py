class Hero:
    def __init__(self,name,life,id,live,weapone):
        self.HeroName = name
        self.HeroId = id
        self.HeroLife = life
        self.HeroLive = live
        self.HeroWeapone = weapone
    def showInfo(self):
        print(self.HeroName,"\t",self.HeroId,"\t",self.HeroLife,"\t",self.HeroLive,"\t",self.HeroWeapone,"\t")
       

x1=Hero("Ting","5000","001","台中","掃把")
x2=Hero("保哥","4500","002","霧峰","微積分課本")
x3=Hero("凱哥","3900","003","高雄","錢包")
x1.showInfo()
x2.showInfo()
x3.showInfo()


"""
print(x.HeroName, "\t",x.HeroId)
print(Hero.__dict__)
print(Hero.__doc__)
print(Hero.__name__)
print(Hero.__module__)
print(Hero.__bases__)
"""