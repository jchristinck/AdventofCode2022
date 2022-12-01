import read_fcns as f

if __name__ == "__main__":
    input = f.read_as_text()
    elves = []
    i = 0
    for j, val in enumerate(input):
        if val:
            input[j] = int(val)
        else:
            input[j] = 0
            elves.append(sum(input[i:j]))
            i = j
    elves.append(sum(input[i:]))
    print(max(elves))
    print(sum(sorted(elves)[-3:]))
