def makeSum():
    file_path = 'dayone1input.txt'
    
    with open(file_path, "r") as file:
        content = file.read()
    
    inputs = content.split("\n")
    sum = 0
    for input in inputs:
        lettered = getNumber(input)
        number = int(lettered[0] + lettered[-1])
        print(number)
        sum += number
    print(sum)


def getNumber(input):
    print(input)
    res = []
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, c in enumerate(input):
        if c.isdigit(): 
            res.append(str(c))
        for num, alpha in enumerate(words):
            if input[i:].startswith(alpha):
                res.append(str(num))
    print(res)
    return res
    
makeSum()