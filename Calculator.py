class Calculator:
    def __init__(self, value=0.0):
        self.value = value
        self.is_iter = False

    def __add__(self, other):
        if type(other) == type(self):
            self.value += other.value
        elif isinstance(other, (int, float)):
            self.value += other
        return self

    def __sub__(self, other):
        if type(other) == type(self):
            self.value -= other.value
        elif isinstance(other, (int, float)):
            self.value -= other
        return self

    def __mul__(self, other):
        if type(other) == type(self):
            self.value *= other.value
        elif isinstance(other, (int, float)):
            self.value *= other
        return self

    def __truediv__(self, other):
        if type(other) == type(self):
            self.value /= other.value
        elif isinstance(other, (int, float)):
            self.value /= other
        return self

    def __pow__(self, power):
        if type(power) == type(self):
            self.value **= power.value
        elif isinstance(power, (int, float)):
            self.value **= power
        return self

    def __setattr__(self, name, value):
        if name in self.__dict__:
            self.__dict__[name] = value
            return
        if len(self.__dict__) < 12:
            self.__dict__[name] = value

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_iter:
            self.is_iter = False
            raise StopIteration
        else:
            self.is_iter = True
            return self.value

    def __repr__(self):
        return 'value: {0}\nattributes:\n{1}'.format(self.value, self.__dict__)