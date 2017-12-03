class Item:
    """
    Клас, котрий моделює річ, що можна покласти в ранець
    """

    weight = 0
    price = 0

    def __init__(self, weight, price):
        self.weight = weight
        self.price = price