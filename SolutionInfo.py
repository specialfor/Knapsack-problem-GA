from Item import Item

class SolutionInfo:

    indexes = []
    stuff = []
    tw = 0
    tp = 0

    def __init__(self, chrom, stuff):
        self.indexes = []
        self.stuff = []
        self.tw = 0
        self.tp = 0

        for i in range(0, len(chrom)):
            if chrom[i] == 1:
                self.indexes.append(i + 1)
                self.stuff.append(stuff[i])
                self.tw += stuff[i].weight
                self.tp += stuff[i].price

    def __repr__(self):
        return f"Indexes: {self.indexes}\nStuff: {self.stuff}\nTotal weight: {self.tw}, total price: {self.tp}"
