from read_input import read_lines

dict_color_limitation = {'red': 12,
                         'green': 13,
                         'blue': 14}

def get_max_cubes_per_color(game_rounds: str) -> bool:
                
    list_game_rounds = game_rounds.split("; ")
    
    list_red = []
    list_green = []
    list_blue = []
           
    for round in list_game_rounds:

        list_cubes = round.split(", ")
        
        for cube in list_cubes:
            cube_colour = cube.split(" ")[1]
            cube_count = int(cube.split(" ")[0])
            
            if cube_colour == 'red':
                list_red.append(cube_count)
            elif cube_colour == 'green': 
                list_green.append(cube_count) 
            else:
                list_blue.append(cube_count)                
            
    max_red = max(list_red)
    max_green = max(list_green) 
    max_blue = max(list_blue) 
    
    power = max_red * max_green * max_blue
                               
    return power  
        
    
def main(path: str) -> int:

    total = 0
    list_games = read_lines(path)
    
    for game in list_games:
            game_rounds = game.split(": ")[1]
            total += get_max_cubes_per_color(game_rounds)
    
    return total

