def make_sum():
    box = [0]

    def add(x):
        box[0] = box[0] + x
        print(box[0])

    return add


s = make_sum()
s(5)
s(3)
s(10)
