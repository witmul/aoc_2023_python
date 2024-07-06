from read_input import read_lines

dict_color_limitation = {'red': 12,
                         'green': 13,
                         'blue': 14}

def check_for_limit_spill(game_rounds: str) -> bool:
    
    limit_spill = False
            
    list_game_rounds = game_rounds.split("; ")
    
    for round in list_game_rounds:
        
        list_cubes = round.split(", ")
        
        for cube in list_cubes:
            cube_colour = cube.split(" ")[1]
            cube_count = int(cube.split(" ")[0])
            
            for limit_color, limit_number in dict_color_limitation.items():
                if cube_colour == limit_color:
                    if cube_count > limit_number:
                        limit_spill = True
                        break
                                 
    return limit_spill  
        
    
def main(path: str) -> int:

    total = 0
    list_games = read_lines(path)
    
    for game in list_games:
        
            game_name = game.split(": ")[0]
            game_id = int(game_name.split(" ")[1])
            game_rounds = game.split(": ")[1]
            
            if not check_for_limit_spill(game_rounds):
                total += game_id
    
    return total

