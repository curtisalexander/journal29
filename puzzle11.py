from string import ascii_lowercase
from functools import reduce

letters = {k+1:v for (k,v) in enumerate(ascii_lowercase)}
initial = [3,25,5,4,11,25,22,3]

def puzzle_test(letters: dict, initial: list, shift: int) -> str:
    return reduce(lambda x, y: x + letters[y], [(x + shift) % 26 + 1 for x in initial], "")

for i in range(26):
    print(puzzle_test(letters, initial, i))