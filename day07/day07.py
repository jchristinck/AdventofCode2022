from pathlib import Path


if __name__ == "__main__":
    text = Path("input.txt").read_text().splitlines()
    tree = {'/': 0}
    current_dir = []
    for idx, row in enumerate(text):
        row = row.split()
        if row[0] == "$":
            if row[1] == "cd":
                if row[2] == "..":
                    current_dir.pop()
                else:
                    if not row[2] in tree.keys():
                        tree[''.join(current_dir) + row[2]] = 0
                    current_dir.append(row[2])
        elif not row[0] == "dir":
            for idy, d in enumerate(current_dir):
                tree[''.join(current_dir[:idy + 1])] += int(row[0])
    print(sum(size for size in tree.values() if size <= 100000))
    print(min(size for size in tree.values() if size > tree['/'] - 4 * 10 ** 7))
