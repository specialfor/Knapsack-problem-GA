from Knapsack import Knapsack
from Item import Item

import matplotlib.pyplot as plt

def draw_plot(index, list):
    plt.figure(index)
    plt.plot(list)
    plt.plot()
    plt.ylabel('average fitness')
    plt.xlabel('index')

#  Вхідні дані
items = [
    Item(3, 1),
    Item(4, 6),
    Item(5, 4),
    Item(8, 7),
    Item(9, 6)
]

w = 13

items2 = [
    Item(6, 5),
    Item(4, 3),
    Item(3, 1),
    Item(2, 3),
    Item(5, 6)
]

w2 = 15

# Клієнтський код
knapsack = Knapsack()
solution1 = knapsack.find_solution(items, w)
print(solution1)
draw_plot(1, knapsack.statistics)

solution2 = knapsack.find_solution(items2, w2)
print(solution2)
draw_plot(2, knapsack.statistics)
plt.show()