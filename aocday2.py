def getSum():
    with open('day2input.txt', "r") as f:
        content = f.read()
    games = content.split("\n")
    sum = 0
    for game in games:
        processed = process(game)
        id = processed[0]
        set = processed[1]
        flag = 1
        gamesum = 1
        for color in set.keys():
            gamesum *= set[color]
        sum += gamesum
    return sum
        
def process(game):
    idandrecord = game.split(": ")
    id = idandrecord[0].split(" ")[1]
    separaterecords = idandrecord[1].split("; ")
    colors = ["blue", "red", "green"]
    maxd = {"red": 0, "blue": 0, "green": 0}
    for record in separaterecords:
        cubes = record.split(", ")
        for cube in cubes:
            for color in colors:
                if color in cube:
                    maxd[color] = max(int(maxd[color]), int(cube.split(" ")[0]))
    return (id,maxd)           
        
print(getSum())
    