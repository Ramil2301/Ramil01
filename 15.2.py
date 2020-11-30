класс животное имя=""

    def eat(self):
        print("Ням-Ням")

    def setAnimalName(self, newName):
        самость.название = новое_имя

    def getAnimalName(self):
        верните себя.имя

    def makeNoize(self):
        печать(self.name, "говорит что-то")

    def _ _ init__(self, newName):
        самость.название = новое_имя
        print("Родилось новое животное " + self.имя)

класс кошка(животное):
    имя=""

    def makeNoize(self):
        печать(self.name, "говорит мяу")

класс Собака(животное):
    имя = ""

    def makeNoize(self):
        печать(self.name, "говорит гав")


my_cat=Cat("Барсик")
мойкот .setAnimalName("Снежок")
print(my_cat.getAnimalName())
мойкот .ешь()
мойкот .макенуаз()

my_dog=Dog("Бобик")
my_dog.setAnimalName("Шарик")
print((my_dog.getAnimalName()))
my_dog.ешь()
my_dog.макенуаз()