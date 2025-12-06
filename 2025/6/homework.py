import math
from distutils.archive_util import make_zipfile


def read_input(file_path):
    input = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            stripped_split_line = line.strip().split(' ')
            input_line = [ entry.strip() for entry in stripped_split_line if entry]
            input.append(input_line)
    return input

def get_operators_and_line_breaks_from_file(line):
    operators = []
    line_breaks = []
    for index, char in enumerate(line):
        if char != ' ':
            operators.append(char)
            line_breaks.append(index)
    return operators, line_breaks

def read_cellophod_input(file_path):
    lines = None
    with open(file_path, 'r') as file:
        lines = [ line for line in file.readlines()]
    if lines is None:
        print("error in reading file")
    longest_line = max(lines, key=len)
    operators, line_breaks = get_operators_and_line_breaks_from_file(lines[-1])
    line_breaks.append(len(longest_line))
    print(f"operators are {operators}")
    print(f"line_break_indices are {line_breaks}")
    operand_lines = []
    for line in lines[:-1]:
        operand_lines.append([ line[line_breaks[index-1]:line_breaks[index]-1 ].replace('\n', ' ') for index in range(1, len(line_breaks)) ])
    print(operand_lines)
    return operators, operand_lines

def do_math(input_data):
    print(input_data)
    row_len = len(input_data)
    col_len = len(input_data[0])
    total = 0
    for index in range(col_len):
        operator = input_data[-1][index]
        operands = [ int(input_data[i][index].strip()) for i in range(row_len-1) ]
        col_total =  sum(operands) if operator == '+' else math.prod(operands)
        print(col_total)
        total += col_total
    return total

def get_cellophod_operands(operand_lines, index):
    max_len = len(operand_lines[0][index])
    # operands = [ operand_line[index] for operand_line in operand_lines]
    index_operands = []
    # print(f"col operands are {operands}")
    for i in range( max_len-1, -1, -1):
        index_operands.append( int(''.join( [ operand_line[index][i] for operand_line in operand_lines ] ) ))
    return index_operands


def do_cellophod_math(operators, operand_lines):
    row_len = len(operand_lines)
    total = 0
    for index, operator in enumerate(operators):
        operands = get_cellophod_operands(operand_lines, index)
        print(f"operands are {operands}, operator is {operator}")
        col_total = sum(operands) if operator == '+' else math.prod(operands)
        print(col_total)
        total += col_total
    return total


def cellophod_math_2(file_path):
    lines = None
    total = 0
    with open(file_path, 'r') as file:
        lines = [ line for line in file.readlines()]
    if lines is None:
        print("error in reading file")
    longest_line = max(lines, key=len)
    max_len = len(longest_line)
    no_of_lines = len(lines)
    operator_line = lines[-1]
    print(lines)
    lines = lines[:-1]
    print(lines)
    operand_stack = []
    skip_next = False
    for i in range(max_len-2, -1, -1):
        # print(f"i is {i}")
        # for line in lines:
        #     print(line[i])
        if skip_next:
            skip_next = False
            continue
        operand_stack.append(int(''.join([line[i] if i < len(line) else ' ' for line in lines])))
        if i < len(operator_line) and operator_line[i]!= ' ':
            operator = operator_line[i]
            print(f"operand stack is {operand_stack}")
            col_total = sum(operand_stack) if operator == '+' else math.prod(operand_stack)
            operand_stack = []
            print(f"col total is {col_total}")
            total += col_total
            skip_next = True
    return total

if __name__ == '__main__':
    # print(do_cellophod_math(read_input("input.txt")))
    print(cellophod_math_2("full_input.txt"))