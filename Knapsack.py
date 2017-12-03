from Chromosome import Chromosome
from SolutionInfo import SolutionInfo
from Item import Item

import random

class Knapsack:
    """
    Клас, котрий розв'язую задачу про ранець використовуючі генетичний алгоритм.
    Для селекції використовується турнірний метод.
    """

    mutation_p = 5  # у відсотках

    tour_part_count = 5  # кількість хромосом, котрі беруть участь в селекції

    pop_count = 200  # кількість популяцій
    chrom_count = 8  # кількість хромосом

    chrom_length = 0  # кількість геній в хромосомі
    chroms = []  # масив хромосом

    stuff = []  # масив речей
    max_weight = 0  # максимальна вага, котру може витримати ранець

    best_chrom = None


    def __init__(self, chrom_count):
        self.chrom_count = chrom_count


    def find_solution(self, stuff, max_weight):
        self.stuff = stuff
        self.chrom_length = len(stuff)

        self.max_weight = max_weight

        self.__perform_algorithm() # запускаємо генетичний алгоритм

        best_chrom = self.__find_best_chrom()  # знаходимо найкращий розв'язок
        selected_stuff = self.__selected_stuff(best_chrom)

        self.stuff = []

        return selected_stuff


    def __perform_algorithm(self):
        """
        Реалізовує генетичний алгоритм
        """
        self.__generate_start_population()  # генерація початкової популяції

        for i in range(0, self.pop_count):
            self.__calculate_fitnesses()  # обчислення здоров'я популяції
            self.__select_next_population()  # генерація нового покоління



    def __generate_start_population(self):
        """
        Генерує початкову популяцію
        """
        for i in range(0, self.chrom_count):
            self.chroms[i] = Chromosome.generate_chromosome(self.chrom_length, 0, 1, True)


    def __calculate_fitnesses(self):
        """
        Обчислює показники здоров'я для всіх хромосом
        """

        # max_index = 0
        for i in range(0, len(self.chroms)):
            chrom = self.chroms[i]
            chrom.fitness = self.__calculate_fitness(chrom)
        #     if chrom.fitness >= self.chroms[max_index]:
        #         max_index = i
        #
        # self.sol_info = SolutionInfo(self.chroms[max_index], )


    def __calculate_fitness(self, chrom):
        """
        Обчислює показник здоров'я для хромосоми (розв'язку) за формулою:

        F(c) = W(c) <= max_weight ? P(c) : 0
        W(c) = sum(Gi.weight), i = 1...n, n - кількість речей
        P(c) = sum(Gi.price), i = 1...n, n - кількість речей

        де P(c) - загальна цінність обраних речей,
        W(c) - загальна вага обраних речей.

        :param chrom: хромосома
        :return: показник здоров'я
        """
        price = 0
        weight = 0

        for i in range(0, len(chrom.gens)):
            gen = chrom[i]
            if gen == 1:
                weight += self.stuff[i].weight
                price += self.stuff[i].price

        if weight <= self.max_weight:
            return price
        else:
            return 0


    def __pairs_for_crossover(self):
        """
        Відбирає пари для розмноження
        :return: список пар, де кожна пара - індекси батьківських хромосом
        """
        pairs = []

        for i in range(0, self.chrom_count):
            first_chrom = self.__find_chrom_by_tournament()
            second_chrom = self.__find_chrom_by_tournament()
            while first_chrom == second_chrom:
                second_chrom = self.__find_chrom_by_tournament()
            pairs.append([first_chrom, second_chrom])

        return pairs


    def __find_chrom_by_tournament(self):
        """
        Знаходить хромосому за допомогою турнірного метода
        :return: індекс хромосоми, що виграла
        """
        best_chrom_index = 0

        for i in range(0, self.tour_part_count):
            rand_chrom_index = random.randint(0, self.chrom_count - 1)
            if self.chroms[rand_chrom_index].fitness >= self.chroms[best_chrom_index].fitness:
                best_chrom_index = rand_chrom_index

        return best_chrom_index


    def __find_best_chrom(self):
        """
        Знаходить найкращу хромосому із популяції
        :return: найкращу хромосому
        """
        best_chrom_index = 0

        for i in range(0, self.chrom_count):
            if self.chroms[i].fitness >= self.chroms[best_chrom_index].fitness:
                best_chrom_index = i

        return self.chroms[best_chrom_index]


    def __select_next_population(self):
        """
        Відбирає наступне покоління
        """
        new_chroms = []

        pairs = self.__pairs_for_crossover()

        new_chroms.append(self.__find_best_chrom())

        for i in range(1, self.chrom_count):
            first_parent = self.chroms[pairs[i][0]]
            second_parent = self.chroms[pairs[i][1]]

            child = first_parent.single_crossover(second_parent)
            child.mutate(self.mutation_p)

            new_chroms.append(child)

        self.chroms = new_chroms


    def __selected_stuff(self, chrom):
        """
        Повертає список речей на основ хромосоми
        :param chrom: хромосома
        :return: список речей
        """
        selected_stuff = []

        for i in range(0, len(chrom.gens)):
            gen = chrom[i]
            if gen == 1:
                selected_stuff.append(self.stuff[i])

        return selected_stuff