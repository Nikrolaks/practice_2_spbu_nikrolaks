class Calculator:
    @staticmethod
    def max_number_of_arguments():
        return 12

    def __init__(self, value=0.0):
        self.value = value
        self.is_iter = False

    def any_operator(self, other, func_of_operator):
        if type(other) == type(self):
            return func_of_operator(other.value)
        elif isinstance(other, (int, float)):
            return func_of_operator(other)

    def __add__(self, other):
        return Calculator(self.any_operator(other, self.value.__add__))

    def __sub__(self, other):
        return Calculator(self.any_operator(other, self.value.__sub__))

    def __mul__(self, other):
        return Calculator(self.any_operator(other, self.value.__mul__))

    def __truediv__(self, other):
        return Calculator(self.any_operator(other, self.value.__truediv__))

    def __pow__(self, power):
        return Calculator(self.any_operator(power, self.value.__pow__))

    def __setattr__(self, name, value):
        if name in self.__dict__:
            self.__dict__[name] = value
            return
        if len(self.__dict__) < self.max_number_of_arguments():
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

