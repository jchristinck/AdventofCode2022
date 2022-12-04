import pathlib


def calc_prio(char):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96


if __name__ == "__main__":
    input = [list(row) for row in pathlib.Path("input.txt").read_text().split('\n')]
    val = 0
    for row in input:
        for char in set(row[:int(len(row) / 2)]) & set(row[int(len(row) / 2):]):
            val += calc_prio(char)
    print(val)
    val = 0
    for i in range(0, len(input) - 3, 3):
        val += calc_prio((set(input[i]) & set(input[i + 1]) & set(input[i + 2])).pop())
    print(val)
