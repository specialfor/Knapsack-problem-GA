class SolutionInfo:

    indexes = []
    stuff = []

    def __init__(self, chrom, stuff):
        self.indexes = []
        self.stuff = []

        for i in range(0, len(chrom)):
            if chrom[i] == 1:
                self.indexes.append(i + 1)
                self.stuff.append(stuff[i])

    def __repr__(self):
        return f"Indexes: {self.indexes}\nStuff: {self.stuff}"
