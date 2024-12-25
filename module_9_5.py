class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step = 1):
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = self.start
    def __iter__(self):
        self.pointer = self.start
        return self
    def __next__(self):
        if self.step > 0 and self.pointer > self.stop or self.step < 0 and self.pointer < self.stop:
            raise StopIteration()
        ptr = self.pointer
        self.pointer += self.step
        return ptr

if __name__ == '__main__':
    iters_attr = [(100, 200, 0),
                  (-5, 1),
                  (6, 15, 2),
                  (5, 1, -1),
                  (10, 10)]
    for attrs in iters_attr:
        try:
            iter_ = Iterator(*attrs)
            for i in iter_:
                print(i, end=' ')
            print()
        except StepValueError:
            print('Шаг указан неверно')