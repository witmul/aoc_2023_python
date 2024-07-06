from read_input import read_lines

def get_number_pair(line: str) -> int:
    
    left_digit = None
    right_digit = None
    
    for ch in line:
        if (ch).isdigit() and left_digit is None:
            left_digit = ch
            break
    
    for ch in reversed(line):    
        if (ch).isdigit() and right_digit is None:
            right_digit = ch
            break
                    
    if left_digit and right_digit:
        digit_pair = int(left_digit + right_digit)
    
    return digit_pair

def main(path: str) -> int:
    
    total = 0
    list_lines = read_lines(path)
    
    for line in list_lines:
        total += get_number_pair(line)
    
    return total