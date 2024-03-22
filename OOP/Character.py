class Character:
    def __init__(self, name, phrase1, phrase2):
        self.name = name
        self.phrase1 = phrase1
        self.phrase2 = phrase2
        self.level = 0

    def speak(self, phraseNum):
        if phraseNum == 1:
            print(self.phrase1)
        else:
            print(self.phrase2)

    def setLevel(self, newLevel):
        self.level = newLevel
        print(f"{self.name}'s new level: {self.level}")


batman = Character("Batman", "I am Batman", "I will protect Gotham City")
batman.speak(1)
batman.setLevel(2)
batman.speak(2)

