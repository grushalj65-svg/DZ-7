def make_plus(a):
    def f(x):
        print(x + a)
    return f


p = make_plus(10)       #Функція яка завжди додає 10
p(5)

q = make_plus(3)
q(7)
