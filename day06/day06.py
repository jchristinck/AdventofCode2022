from pathlib import Path
import collections


def find_x_unique_elements(text, num, message):
    buffer = collections.deque(maxlen=num)
    for idx, char in enumerate(text):
        buffer.append(char)
        if len(set(buffer)) == num:
            print(message, idx)
            break


if __name__ == "__main__":
    text = Path("input.txt").read_text()
    find_x_unique_elements(text, 4, 'start of packet: ')
    find_x_unique_elements(text, 14, 'start of message: ')
