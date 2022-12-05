from pathlib import Path
import copy


if __name__ == "__main__":
    text = [x for x in Path("input.txt").read_text().splitlines() if x]
    stack_end = False
    stacks = [[]]
    for row in text:
        if row[1].isdecimal():
            stack_end = True
            for idx, stack in enumerate(stacks):
                stacks[idx] = stack[::-1]
                for idy, char in enumerate(stacks[idx]):
                    if char == ' ':
                        stacks[idx] = stacks[idx][:idy]
            stacks_alt = copy.deepcopy(stacks)
            continue
        if stack_end:
            row = list(map(int, filter(lambda x: x.isnumeric(), row.split())))
            moves = row[0]
            while moves > 0:
                moves -= 1
                stacks[row[2] - 1].append(stacks[row[1] - 1].pop())
                stacks_alt[row[2] - 1].append(stacks_alt[row[1] - 1].pop())
            stacks_alt[row[2] - 1][-row[0]:] = reversed(stacks_alt[row[2] - 1][-row[0]:])
        else:
            for i in range(1, len(row), 4):
                if int(i / 4) > len(stacks) - 1:
                    stacks.append([])
                stacks[int(i / 4)].append(row[i])
    tops = ''
    tops_alt = ''
    for stack in stacks:
        tops += stack[-1]
    for stack in stacks_alt:
        tops_alt += stack[-1]
    print(tops)
    print(tops_alt)
