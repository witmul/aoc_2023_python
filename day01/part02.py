from read_input import read_lines

dict_word_digit = {'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'}


def get_left_digit(line: str) -> str:
    
    for i in range (len(line)):
        if line[i].isdigit():
            return line[i]
        
        substr = line[:i + 1]
        
        for word, digit in dict_word_digit.items():
            if word in substr:
                return digit

def get_right_digit(line: str) -> str:
    
    for i in range (len(line)):
        rev_i = -(i+1)
        if line[rev_i].isdigit():
            return line[rev_i]
        
        substr = line[rev_i:]
        
        for word, digit in dict_word_digit.items():
            if word in substr:
                return digit    

def get_number_pair(line: str) -> int:
    left_digit = get_left_digit(line)
    right_digit = get_right_digit(line)
    digit_pair = int(left_digit + right_digit)
    return digit_pair

def main(path: str) -> int:
    
    total = 0
    list_lines = read_lines(path)

    for line in list_lines:
        total += get_number_pair(line)

    return print(total)