
def main():
    print("Test")

    # Rules: 12 red cubes, 13 green cubes, and 14 blue cubes
    red_rules = 12
    green_rules = 13
    blue_rules = 14

    with open("D:\\Sandbox\AdventCode\Day2\input1.txt") as file:
        lines = [line.strip() for line in file]


    color_cubes = []
    for word in lines:
        w = word.split(':')[1]
        color_cubes.append(w)
    
    valid_games = []
    fewest_nums = []
    for game in color_cubes:
        round = color_cubes.index(game)+1
        print(game)
        sec = game.split(';')
        valid = True
        max_red = 1
        max_green = 1
        max_blue = 1
        for s in sec:
            show = s.split(',')
            for el in show:
                abc = el.strip().split(' ')
                if abc[1] == 'blue':
                    val = int((el.split('blue'))[0].strip())
                    if val > max_blue:
                        max_blue = val
                    if val > blue_rules:
                        valid = False

                elif abc[1] == 'red':
                    val = int((el.split('red'))[0].strip())
                    if val > max_red:
                        max_red = val
                    if val > red_rules:
                        valid = False
                elif abc[1] == 'green':
                    val = int((el.split('green'))[0].strip())
                    if val > max_green:
                        max_green = val
                    if val > green_rules:
                        valid = False
                    
                
        if(valid):
            valid_games.append(round)
        
        fewest_nums.append(max_red*max_blue*max_green)
                
    print(f"Answer for first part: {sum(valid_games)} ")
    print(f"Answer for second part: {sum(fewest_nums)} ")
                
                


if __name__ == "__main__":
    main()