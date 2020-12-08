# How To get total combinations which can be made with min length and max length
from itertools import chain, combinations
min_len = int(input("Min Len: "))
max_len = int(input("Max Len: "))
characters = str(input("Characters To use: "))
combination = list(chain.from_iterable(combinations(characters, i) for i in range(min_len, max_len+1)))
for comb in combination:
    print("".join(comb))
