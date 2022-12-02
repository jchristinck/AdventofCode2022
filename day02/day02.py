import read_fcns as f

if __name__ == "__main__":
    input = f.read_as_text()
    part_a = 0
    part_b = 0
    for row in input:
        row = row.split()
        if row[0] == 'A':
            if row[1] == 'X':
                part_a += 4
                part_b += 3
            elif row[1] == 'Y':
                part_a += 8
                part_b += 4
            else:
                part_a += 3
                part_b += 8
        elif row[0] == 'B':
            if row[1] == 'X':
                part_a += 1
                part_b += 1
            elif row[1] == 'Y':
                part_a += 5
                part_b += 5
            else:
                part_a += 9
                part_b += 9
        else:
            if row[1] == 'X':
                part_a += 7
                part_b += 2
            elif row[1] == 'Y':
                part_a += 2
                part_b += 6
            else:
                part_a += 6
                part_b += 7
    print(part_a)
    print(part_b)

