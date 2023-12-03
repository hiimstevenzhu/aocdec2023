with open("day3/day3input.txt", "r") as file:
    content = file.read()
    
nonSym = "."
lines = content.split('\n')
mtx = [0] * len(lines)
for idx in range(len(lines)):
    mtx[idx] = lines[idx]
print(mtx)
potential = []
for i in range(len(mtx)):
    j = 0 
    while (j < len(mtx[i])):
        cluster = ""
        if mtx[i][j].isdigit():
            cluster += mtx[i][j]
            temp = j+1
            while temp < len(mtx[i]) and mtx[i][temp].isdigit():
                cluster += mtx[i][temp]
                temp += 1
            print(cluster)
        if cluster:
            checked = 0
            for idx in range(j, temp):
                for a in range(-1,2):
                    for b in range(-1, 2):
                        if 0 <= (i+a) < len(mtx) and 0 <= idx + b < len(mtx[i]):
                            if not mtx[i+a][idx+b].isdigit() and mtx[i+a][idx+b] != nonSym:
                                if not checked: 
                                    potential.append(int(cluster))
                                    checked = 1
        
        if cluster:
            j = temp 
        else:
            j += 1
                
print(sum(potential))
     
    