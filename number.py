
class Number:
    def __init__(self, x, base=10):
        if isinstance(x, str):
            self.x = int(x, base=base)
        else:
            self.x = int(x)
        self.base = base

    def __str__(self):
        if self.base == 10:
            return f"{self.x}"

        si = "-" if self.x < 0 else ""
        return si + self.__convert(abs(self.x))

    @staticmethod
    def __op__(x, y, operator):
        if isinstance(x, int):
            if isinstance(y, int):
                return Number(operator(x, y))
            elif isinstance(y, Number):
                return Number(operator(x, y.x), y.base)
            elif isinstance(y, float):
                return operator(x, y)
        elif isinstance(x, Number):
            if isinstance(y, int):
                return Number(operator(x.x, y), x.base)
            elif isinstance(y, Number):
                return Number(operator(x.x, y.x), x.base)
            elif isinstance(y, float):
                return operator(x.x, y)

        elif isinstance(x, float):
            if isinstance(y, int):
                return operator(x, y)
            elif isinstance(y, Number):
                return operator(x, y.x)
            elif isinstance(y, float):
                return operator(x, y)

        raise TypeError


    def __add__(self, o):
        return self.__op__(self, o, lambda x, y: x + y)

    def __radd__(self, o):
        return self + o

    def __sub__(self, o):
        return self.__op__(self, o, lambda x, y: x - y)

    def __rsub__(self, o):
        return self.__op__(o, self, lambda x, y: x - y)

    def __mul__(self, o):
        return self.__op__(self, o, lambda x, y: x * y)

    def __rmul__(self, o):
        return self * o

    def __floordiv__(self, o):
        return self.__op__(self, o, lambda x, y: x // y)

    def __rfloordiv__(self, o):
        return self.__op__(o, self, lambda x, y: x // y)

    def __truediv__(self, o):
        return self.__op__(float(self.x), o, lambda x, y: x / y)

    def __rtruediv__(self, o):
        return self.__op__(o, float(self), lambda x, y: x / y)

    def __mod__(self, o):
        return self.__op__(self, o, lambda x, y: x % y)

    def __rmod__(self, o):
        return self.__op__(o, self, lambda x, y: x % y)

    def __convert(self, k):
        asc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        strr = lambda x: str(x) if x < 10 else asc[x - 10]

        q = k // self.base
        r = k % self.base

        if (q == 0):
            return strr(r)
        return self.__convert(q) + strr(r)

    def sum_digits(self):
        return Number(sum(map(lambda x: int(x, base=self.base), str(self))), base=self.base)




