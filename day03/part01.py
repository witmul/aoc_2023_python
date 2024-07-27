
def read_input(path: str) -> list:
    with open(path, "r") as f:
        return [line.strip() for line in f]

def check_adjusted_symbol(engine_schematic: list[str], row_id: int, start: int, end: int) -> bool:
    # Check right side
    if end < len(engine_schematic[row_id]) - 1:
        end += 1  # <- adding 1 to also check diagonaly (up/down right) later
        if engine_schematic[row_id][end] != ".":
            return True
    # Check left side
    if start > 0:
        start -= 1  # <- removing 1 to also check diagonaly (up/down left) later
        if engine_schematic[row_id][start] != ".":
            return True
    # Check below
    if row_id > 0:
        for i in range(start, end + 1):
            char = engine_schematic[row_id - 1][i]
            if char != "." and not char.isdigit():
                return True
    # Check up
    if row_id < len(engine_schematic) - 1:
        for i in range(start, end + 1):
            char = engine_schematic[row_id + 1][i]
            if char != "." and not char.isdigit():
                return True

    return False

def main(path: str) -> int:
    total = 0
    engine_schematic = read_input(path)
    
    for r_i, row in enumerate(engine_schematic):
        number = ""
        row_size = len(row)
        
        for c_i, char in enumerate(row):
            if char.isdigit():
                number += char
                is_end = c_i == row_size - 1

                if is_end and check_adjusted_symbol(engine_schematic, r_i, c_i - len(number) + 1, c_i):
                    total += int(number)
            elif number != '':
                if check_adjusted_symbol(engine_schematic, r_i, c_i - len(number), c_i - 1):
                    total += int(number)
                number = ""
    
    return total