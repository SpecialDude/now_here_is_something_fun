from .number import Number
import time

SLEEP = 0.15

def sum_digits(num):
    if num / 10 < 1:
        return num
    return (num % 10) + sum_digits(num // 10)

def sum_digitss(num):
    return sum_digits(num) if not isinstance(num, Number) else num.sum_digits()

def recursive_sum_digits(num, echo=True, sep="", end="", just=str.ljust, jn=0):

    if isinstance(num, Number):
        k = num.sum_digits()

        if k / k.base < 1:
            if echo:
                print(just(f"{' + '.join(list(str(num)))} = [\033[1;33m{k}\033[0m]", jn), end="")
            return k

        if echo:
            print(just(f"{' + '.join(list(str(num)))} = {k}", jn), end="")
    else:
        k = sum_digits(num)

        if k / 10 < 1:
            if echo:
                print(just(f"{' + '.join(list(str(num)))} = [\033[1;33m{k}\033[0m]", jn), end="")
            return k

        if echo:
            print(just(f"{' + '.join(list(str(num)))} = {k}", jn), end="")


    if echo:
        print(sep, end="")

    return recursive_sum_digits(k, echo, sep, end, just, jn=20)




def print9():
    print(list(map(lambda x : sum_digits(x * 9), range(1, 10))))

def generate_multi_table(num=9, max=121):
    pad = len(str(max)) if isinstance(num, int) else len(str(Number(max, base=num.base)))
    mpad = len(str(num * max))
    mmpad = len(' + '.join(list(str(num * max))))
    mmmpad = len(str(sum_digitss(num * max)))

    print( "                             ╔------------------------╗")
    print(f"                             ║\033[1;32m{f'Base {num.base} Number System'.center(24)}\033[0m║")
    print( "                             ╚------------------------╝\n")

    for i in range(max + 1):
        if isinstance(num, Number):
            i = Number(i, base=num.base)
        mul = i * num
        # print(f"{str(i).ljust(pad)} x {num} = {str(mul).ljust(mpad)} --> {' + '.join(list(str(mul))).ljust(mmpad)} = {str(recursive_sum_digits(mul)).ljust(mmmpad)}")
        time.sleep(SLEEP)

        print(f"{str(i).rjust(pad)} × {num} = {str(mul).rjust(mpad)}    -->    ", end="")
        s = recursive_sum_digits(mul, echo=True, sep="    -->    ", end="", jn=mmpad+6+mmmpad, just=str.ljust)
        print()