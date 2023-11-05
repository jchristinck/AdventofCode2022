from pathlib import Path

def check_view_distance(elements_to_check, el, pos_el, length):
            for idz, i in elements_to_check:
                if i >= el:
                    return abs(pos_el - idz)
                if not idz: return pos_el
                if idz == length: return length - pos_el
            return 0

if __name__ == "__main__":
    trees = [[eval(col) for col in row] for row in Path("input.txt").read_text().splitlines()]
    length = len(trees) - 1
    vis_from_outside = 0
    highest_scenic_score = 0
    for idy, row in enumerate(trees):
        for idx, el in enumerate(row):
            col = [row[idx] for row in trees]
            if not idy or not idx or idy == len(trees) - 1 or idx == len(row) - 1: #edge
                vis_from_outside += 1
            elif max(row[:idx]) < el: #check left
                vis_from_outside += 1
            elif max(row[idx + 1:]) < el: #check right
                vis_from_outside += 1
            elif max(col[:idy]) < el: #check top
                vis_from_outside += 1
            elif max(col[idy + 1:]) < el:#check bottom
                vis_from_outside += 1
            d_left = check_view_distance( reversed(list(enumerate(row[:idx]))), el, idx, length)
            d_right = check_view_distance(enumerate(row[idx + 1:], start=idx+1), el, idx, length)
            d_top = check_view_distance( reversed(list(enumerate(col[:idy]))), el, idy, length)
            d_bottom = check_view_distance(enumerate(col[idy + 1:], start=idy+1), el, idy, length)
            highest_scenic_score = max(d_left * d_right * d_top * d_bottom, highest_scenic_score)

    print(vis_from_outside)
    print(highest_scenic_score)