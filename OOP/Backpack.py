class Backpack:
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.items = []
        self.open = False

    def openBag(self):
        self.open = True
        print("Backpack is open")

    def closeBag(self):
        self.open = False
        print("Backpack is closed")

    def putIn(self, item):
        if self.open:
            self.items.append(item)
            print(f"Here are all your items: {', '.join(self.items)}")
        else:
            print("Backpack is closed. Can't add items to it")

    def takeOut(self, item):
        if self.open:
            self.items.remove(item)
            print(f"Here are all your items: {', '.join(self.items)}")
        else:
            print("Backpack is closed. Can't remove items from it")


smallBlueBackpack = Backpack("blue", "small")
mediumRedBackpack = Backpack("red", "medium")
largeGreenBackpack = Backpack("green", "large")

largeGreenBackpack.openBag()
largeGreenBackpack.putIn("lunch")
largeGreenBackpack.putIn("jacket")
largeGreenBackpack.closeBag()
largeGreenBackpack.openBag()
largeGreenBackpack.takeOut("jacket")
largeGreenBackpack.closeBag()

