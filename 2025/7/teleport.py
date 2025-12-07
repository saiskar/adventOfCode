from collections import defaultdict
from itertools import count


def read_file(file_path):
    with open(file_path, 'r') as file:
        return [ line.strip() for line in file.readlines()]


def get_tachyon_entry(input):
    row_len = len(input)
    col_len = len(input[0])
    for row_index in range(row_len):
        for col_index in range(col_len):
            if input[row_index][col_index] == 'S':
                return row_index, col_index
    return -1, -1

def no_of_splits(input):
    row_len = len(input)
    col_len = len(input[0])
    split_count = 0
    tachyon_row_index, tachyon_col_index = get_tachyon_entry(input)
    tachyon_col_indices = set([tachyon_col_index])
    for row_index in range(tachyon_row_index, row_len-1):
        indices_to_add = set()
        indices_to_remove = set()
        for tachyon_col_index in tachyon_col_indices:
            if input[row_index+1][tachyon_col_index] == '^':
                split_count += 1
                if tachyon_col_index -1 >= 0:
                    indices_to_add.add(tachyon_col_index-1)
                if tachyon_col_index + 1 < col_len:
                    indices_to_add.add(tachyon_col_index+1)
                indices_to_remove.add(tachyon_col_index)
        tachyon_col_indices -= indices_to_remove
        tachyon_col_indices |= indices_to_add
        print(f"for row {row_index}, no of splits is {indices_to_add}")
        print(f"updated split count is {split_count}")
    return split_count


def no_of_timelines(input):
    row_len = len(input)
    col_len = len(input[0])
    tachyon_row_index, tachyon_col_index = get_tachyon_entry(input)
    tachyon_col_indices = set([tachyon_col_index])
    timelines_dict = { tachyon_col_index : 1 }
    print(timelines_dict)
    for row_index in range(tachyon_row_index, row_len - 1):
        new_timelines_dict = defaultdict(int)
        indices_to_add = set()
        indices_to_remove = set()
        for tachyon_col_index in tachyon_col_indices:
            if input[row_index + 1][tachyon_col_index] == '^':
                if tachyon_col_index - 1 >= 0:
                    new_timelines_dict[tachyon_col_index-1] += timelines_dict[tachyon_col_index]
                    indices_to_add.add(tachyon_col_index - 1)
                if tachyon_col_index + 1 < col_len:
                    new_timelines_dict[tachyon_col_index + 1] += timelines_dict[tachyon_col_index]
                    indices_to_add.add(tachyon_col_index + 1)
                indices_to_remove.add(tachyon_col_index)
            else:
                new_timelines_dict[tachyon_col_index] += timelines_dict[tachyon_col_index]
        tachyon_col_indices -= indices_to_remove
        tachyon_col_indices |= indices_to_add
        print(f"timelines dict is {timelines_dict}")
        print(f"new timelines dict is {new_timelines_dict}")
        timelines_dict = new_timelines_dict

    print(timelines_dict)
    timelines = 0
    for k,v in timelines_dict.items():
        timelines += v
    print(timelines)
    return timelines


if __name__ == '__main__':
    input = read_file('full_input.txt')
    print(no_of_timelines(input))