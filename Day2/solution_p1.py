
def main():
    print("Test")

    # Rules: 12 red cubes, 13 green cubes, and 14 blue cubes
    red_rules = 12
    green_rules = 13
    blue_rules = 14

    with open("D:\\Sandbox\AdventCode\Day2\input2.txt") as file:
        lines = [line.strip() for line in file]


    color_cubes = []
    for word in lines:
        w = word.split(':')[1]
        color_cubes.append(w)
    
    valid_games = []
    for game in color_cubes:
        round = color_cubes.index(game)+1
        print(game)
        sec = game.split(';')
        valid = True
        for s in sec:
            if not valid:
                break
            show = s.split(',')
            for el in show:
                abc = el.strip().split(' ')
                if abc[1] == 'blue':
                    val = el.split('blue')
                    if int(val[0].strip()) > blue_rules:
                        valid = False
                        break

                elif abc[1] == 'red':
                    val = el.split('red')
                    if int(val[0].strip()) > red_rules:
                        valid = False
                        break
                elif abc[1] == 'green':
                    val = el.split('green')
                    if int(val[0].strip()) > green_rules:
                        valid = False
                        break
                    
                
        if(valid):
            valid_games.append(round)
                
    # print(valid_games)
    print(sum(valid_games))
                
                


if __name__ == "__main__":
    main()