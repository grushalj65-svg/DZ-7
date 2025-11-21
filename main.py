class Pow2:
    def __init__(self, stop):         #Максимальний показник степеня.
        self.stop = stop

    def show(self):
        p = 0
        v = 1
        while p <= self.stop:          #Працює, поки степінь не досягне stop.
            print(v)
            v = v * 2
            p = p + 1


Pow2(5).show()
