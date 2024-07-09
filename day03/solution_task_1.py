def read_input(path: str) -> list:
    with open(path, "r") as f:
        return [line.strip() for line in f]

# class Digit:
#     def __init__(self, x, y) -> None:
#         self.coor_x = x
#         self.coor_y = y
        

# def check_if_special_char(char: str) -> bool:
#     return char != "." and not char.isdigit()

# def get_whole_digit():
#     return

# def check_around(path: str):
    


# def get_part_numbers(line: str):
#     for i, char in enumerate(line):
#         start = 0
#         whole_digit = ""
#         if char.isdigit():
#             substr = line[:i]
#     return



def main(path: str) -> int:
    total = 0
    engine_schematic = read_input(path)
    
    for line_id, line in enumerate(engine_schematic):
            
            digit_start = 0
            digit_end = 0
            
            for i, char in enumerate(line):
                digit_end = digit_end + 1
                if char.isdigit():
                    substr = line[digit_start:digit_end]
                else:
                    digit_start = digit_end

                    # end += 1
                    # do a check around
                    # line_id as x (row) and i as y (column)
                    
                    # x = line_id
                    # y = i
                    
                    # if x == 0:
                    #     if y == 0:
                    #         adj_y = (0,2)
                    #         next_line = engine_schematic[x+1]
                        
                    
                    

    return


if __name__ == "__main__":
    main("day03/test_input.txt")
