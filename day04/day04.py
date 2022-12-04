import pathlib


if __name__ == "__main__":
    input = [list(map(int, row.replace('-', ',').split(','))) for row in list(filter(None, pathlib.Path("input.txt").read_text().split('\n')))]
    print(sum((row[3] - row[1]) * (row[2] - row[0]) < 1 for row in input))
    print(sum(len(list(set(range(row[0], row[1] + 1)) & set(range(row[2], row[3] + 1)))) > 0 for row in input))
