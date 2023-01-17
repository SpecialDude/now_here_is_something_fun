from now_here_is_something_fun import *
import os, platform

intro = "Behaviour of Radix-Minus-One Digit in each Number Base Systems"

system = platform.system()
if system == "Windows":
    os.system("cls")
elif system in ("Linux", "Darwin"):
    os.system("clear")

w, h = os.get_terminal_size()
print("\n" * h)

print(intro.center(w))

for _ in range(h//3):
    print()
    time.sleep(SLEEP)


for i in range(2, 37):
    generate_multi_table(Number(i-1, base=i), max=50)
    print("\n\n")


# k = Number("D2", base=16)

# print(k.sum_digits())

