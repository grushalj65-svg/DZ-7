class Words:
    def __init__(self, data):
        self.data = data

    def show(self):         #виводимо довжини всіх слів.
        i = 0
        while i < self.count_items():
            w = self.data[i]              #Перебирає кожен символ слова.
            c = 0
            for _ in w:
                c = c + 1
            print(c)
            i = i + 1

    def count_items(self):
        k = 0
        for _ in self.data:
            k = k + 1
        return k


Words(["apple", "banana", "kiwi"]).show()

