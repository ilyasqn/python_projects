class Sklad:
    def __init__(self, name, stuff):
        self.name = name
        self.stuff = stuff
        self.bag = {self.name: self.stuff}

    def adding(self, add_name, add_stuff):
        self.add_name = add_name
        self.add_stuff = add_stuff
        for key in self.bag.keys():
            if key == self.add_name:
                self.add_stuff += self.bag.get(key)
                self.bag.update({key: self.add_stuff})
        else:
            self.bag.update({self.add_name: self.add_stuff})

    def deleting(self, del_name, del_stuff):
        self.del_name = del_name
        self.del_stuff = del_stuff
        for key in self.bag.keys():
            if key == self.del_name:
                self.del_stuff -= self.bag.get(key)
                self.bag.update({key: self.del_stuff})
        else:
            self.bag.update({self.del_name: abs(self.del_stuff)})

    def get_value(self):
        print(self.bag)


sklad1 = Sklad("First", 25)
sklad1.adding("Third", 12)
sklad1.adding("First", 10)
sklad1.adding("Third", 10)
sklad1.adding("Four", 40)

sklad1.deleting("Four", 10)
sklad1.deleting("First", 15)
sklad1.deleting("Third", 10)

sklad1.get_value()


sklad2 = Sklad("First", 25)
sklad2.adding("First", 15)
sklad2.adding("Third", 30)
sklad2.adding("Third", 10)

sklad2.deleting("First", 10)
sklad2.deleting("Third", 10)

sklad2.get_value()

