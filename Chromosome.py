import random

class Chromosome:
    """
    Цей клас моделює хромосому
    """
    gens = []

    def __getitem__(self, index):
        return self.gens[index]


    def __setitem__(self, index, gen):
        self.gens[index] = gen


    def generate_chromosome(length, min, max, isInt):
        chromosome = Chromosome()

        for i in range(0, length):
            if isInt:
                chromosome.gens[i] = random.randint(min, max)
            else:
                chromosome.gens[i] = random.uniform(min, max)

        return chromosome