import random
from copy import deepcopy


class Chromosome:
    """
    Цей клас моделює хромосому
    """
    gens = []
    fitness = 0

    min_value = 0
    max_value = 0

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    # Перевизначення оператора []
    def __getitem__(self, index):
        """
        Повертає ген за індексом
        :param index: індекс
        :return: ген
        """
        return self.gens[index]

    def __setitem__(self, index, gen):
        """
        Замінює ген за індексом
        :param index: індекс
        :param gen: новий ген
        """
        self.gens[index] = gen


    def __len__(self):
        """
        :return: кількість генів в хромосомі
        """
        return len(self.gens)

    # Схрещення
    def __random_cross_line(self):
        """
        Генерує рандомну точку для схрещення
        :return: номер гена після якого відбудиться схрещення
        """
        return random.randint(0, len(self.gens) - 2)

    def single_crossover(self, second_chrom):
        """
        Схрещує дві хромосоми. Використовує 'double_crossover(self, second_chrom)' метод.
        Дитина обирається випадково.
        :param second_chrom: друга хромосома
        :return: дитина
        """
        index = random.randint(0, 1)
        children = self.double_crossover(second_chrom)
        return children[index]

    def double_crossover(self, second_chrom):
        """
        Схрещує дві хромосоми.
        :param second_chrom: друга хромосома
        :return: масив з 2 дітьми
        """
        line = self.__random_cross_line()

        first_child = deepcopy(self)
        second_child = deepcopy(second_chrom)

        for i in range(0, len(self.gens)):
            if i > line:
                first_child[i] = second_chrom[i]
                second_child[i] = self[i]

        return [first_child, second_child]

    # Мутація
    def mutate(self, likelihood):
        """
        Мутує гени в хромосомі з заданою ймовірністю
        :param likelihood: ймовірність мутації у відсотках
        """
        for i in range(0, len(self.gens)):
            rand = random.uniform(0, 100)
            if rand <= likelihood:
                self.__mutate_gen(i)

    def __mutate_gen(self, gen_index):
        """
        Мутує ген за індексом
        :param gen_index: індекс гена
        """
        new_gen = self[gen_index]
        while new_gen == self[gen_index]:
            new_gen = random.randint

    # Генерація хромосоми
    @classmethod
    def generate_chromosome(cls, length, min_value, max_value, is_int):
        """
        Генерує випадкову хромосому
        :param length: кількість генів
        :param min: мінімальне значення гена
        :param max: максимальне значення гена
        :param is_int: використовувати значення цілого типу
        :return:
        """
        chromosome = Chromosome(min_value, max_value)
        chromosome.gens = []
        for i in range(0, length):
            chromosome.gens.append(None)

        for i in range(0, length):
            if is_int:
                chromosome[i] = random.randint(min_value, max_value)
            else:
                chromosome[i] = random.uniform(min_value, max_value)

        return chromosome
